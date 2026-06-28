import firebase_admin
from firebase_admin import credentials, auth
from src.app.core.config import settings

# Initialize Firebase Admin SDK
try:
    if not firebase_admin._apps:
        if settings.FIREBASE_CLIENT_EMAIL and settings.FIREBASE_PRIVATE_KEY:
            cred = credentials.Certificate({
                "type": "service_account",
                "project_id": settings.FIREBASE_PROJECT_ID,
                "private_key_id": settings.FIREBASE_PRIVATE_KEY_ID,
                "private_key": settings.FIREBASE_PRIVATE_KEY.replace("\\n", "\n"),
                "client_email": settings.FIREBASE_CLIENT_EMAIL,
            })
            firebase_admin.initialize_app(cred)
        else:
            # Fallback for local testing or credentials loaded from default Google context
            firebase_admin.initialize_app()
except Exception as e:
    # Allow application to boot in mock mode if Firebase environment variables are not set yet
    print(f"Warning: Firebase initialization failed. Mock auth may be required: {e}")


def verify_firebase_token(token: str) -> dict:
    """
    Verifies a Firebase ID token.
    In development mode with missing credentials, it can return a dummy profile.
    """
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        if settings.ENVIRONMENT == "development":
            # Mock verification for testing without config
            print(f"Firebase token verify failed ({e}). Returning dev mock user.")
            return {"uid": "mock-dev-user-id", "email": "dev@joborbit.com"}
        raise e
