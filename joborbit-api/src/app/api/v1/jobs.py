from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.app.core.database import get_db
from src.app.core.security import get_current_user
from src.app.schemas.job import JobApplicationResponse, JobApplicationCreate, JobApplicationUpdate
from src.app.models.job import JobApplication

router = APIRouter()


@router.get("/", response_model=List[JobApplicationResponse])
def get_job_applications(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    uid = current_user.get("uid")
    return db.query(JobApplication).filter(JobApplication.user_id == uid).all()


@router.post("/", response_model=JobApplicationResponse, status_code=status.HTTP_201_CREATED)
def create_job_application(
    job_in: JobApplicationCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    uid = current_user.get("uid")
    db_job = JobApplication(**job_in.model_dump(), user_id=uid)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
