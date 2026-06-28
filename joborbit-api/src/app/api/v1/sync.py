from fastapi import APIRouter, Depends
from src.app.core.security import get_current_user

router = APIRouter()


@router.post("/gmail")
async def sync_emails(
    current_user: dict = Depends(get_current_user)
):
    """
    Syncs recruiter emails from user's linked Gmail inbox.
    """
    # Google API logic will go here
    return {"status": "success", "synced_count": 0}


@router.post("/calendar")
async def sync_calendar(
    current_user: dict = Depends(get_current_user)
):
    """
    Schedules/syncs interviews in Google Calendar.
    """
    # Google Calendar integration logic will go here
    return {"status": "success", "synced_count": 0}
