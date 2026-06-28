from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from src.app.core.config import settings


def get_google_services(token_info: dict):
    """
    Builds and returns Google Gmail and Calendar client services using the user OAuth2 credentials.
    """
    creds = Credentials(
        token=token_info.get("access_token"),
        refresh_token=token_info.get("refresh_token"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=settings.GOOGLE_CLIENT_ID,
        client_secret=settings.GOOGLE_CLIENT_SECRET,
        scopes=[
            "https://www.googleapis.com/auth/gmail.readonly",
            "https://www.googleapis.com/auth/calendar"
        ]
    )

    gmail_service = build("gmail", "v1", credentials=creds)
    calendar_service = build("calendar", "v3", credentials=creds)

    return gmail_service, calendar_service
