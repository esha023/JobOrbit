from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.app.services.firebase import verify_firebase_token

security_scheme = HTTPBearer()


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security_scheme)):
    """
    Dependency to verify Firebase ID tokens passed in the Authorization header.
    Returns the parsed user payload containing 'uid', 'email', etc.
    """
    token = credentials.credentials
    try:
        decoded_token = verify_firebase_token(token)
        if not decoded_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials or expired session",
            )
        return decoded_token
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Authentication failed: {str(e)}",
        )
