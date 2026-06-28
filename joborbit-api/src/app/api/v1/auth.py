from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.app.core.database import get_db
from src.app.core.security import get_current_user
from src.app.schemas.user import UserResponse, UserCreate
from src.app.models.user import User

router = APIRouter()


@router.post("/sync-user", response_model=UserResponse, status_code=status.HTTP_200_OK)
def sync_user(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Onboards a user onto the local SQL database by matching their Firebase authentication credentials.
    """
    uid = current_user.get("uid")
    email = current_user.get("email")
    name = current_user.get("name", "")

    user = db.query(User).filter(User.id == uid).first()
    if not user:
        user = User(id=uid, email=email, display_name=name)
        db.add(user)
        db.commit()
        db.refresh(user)

    return user
