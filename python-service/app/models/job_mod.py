from sqlalchemy import Column, Integer, String, Text, DateTime, DECIMAL, ARRAY
from database import Base
import uuid
from datetime import datetime

class JobStatus:
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String(36), unique=True, default=lambda: str(uuid.uuid4()))
    text_content = Column(Text, nullable=False)
    status = Column(String(20), default=JobStatus.PENDING)
    sentiment_score = Column(DECIMAL(3, 2), nullable=True)
    keywords = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
