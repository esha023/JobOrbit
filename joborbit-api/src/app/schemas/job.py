from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime


class JobApplicationBase(BaseModel):
    company: str
    position: str
    status: str = "WISHLIST"
    salary: Optional[int] = None
    location: Optional[str] = None
    url: Optional[str] = None
    applied_date: Optional[datetime] = None
    notes: Optional[str] = None


class JobApplicationCreate(JobApplicationBase):
    pass


class JobApplicationUpdate(BaseModel):
    company: Optional[str] = None
    position: Optional[str] = None
    status: Optional[str] = None
    salary: Optional[int] = None
    location: Optional[str] = None
    url: Optional[str] = None
    applied_date: Optional[datetime] = None
    notes: Optional[str] = None


class JobApplicationResponse(JobApplicationBase):
    id: int
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
