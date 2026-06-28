from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime, func
from src.app.core.database import Base


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    company = Column(String, nullable=False, index=True)
    position = Column(String, nullable=False)
    status = Column(String, default="WISHLIST")  # WISHLIST, APPLIED, INTERVIEWING, OFFERED, REJECTED
    salary = Column(Integer, nullable=True)
    location = Column(String, nullable=True)
    url = Column(String, nullable=True)
    applied_date = Column(DateTime, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
