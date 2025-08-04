# app/models/job.py
from sqlalchemy import Column, String, Text, DateTime, DECIMAL, ARRAY
from database import Base
import uuid
from datetime import datetime

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True)
    job_id = Column(String(36), unique=True, default=lambda: str(uuid.uuid4()))
    text_content = Column(Text, nullable=False)
    status = Column(String(20), default="PENDING")
    sentiment_score = Column(DECIMAL(3,2))
    keywords = Column(ARRAY(String))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

# app/services/job_service.py
class JobService:
    def __init__(self, job_repository, analysis_client):
        self.job_repository = job_repository
        self.analysis_client = analysis_client
    
    def submit_job(self, text_content: str) -> str:
        # Función pura para validación
        if not self._is_valid_text(text_content):
            raise ValueError("Invalid text content")
        
        job = Job(text_content=text_content)
        self.job_repository.save(job)
        
        # Llamada síncrona al servicio Java
        self.analysis_client.start_analysis(job.job_id)
        
        return job.job_id
    
    def _is_valid_text(self, text: str) -> bool:
        # Función pura - mismo input, mismo output, sin efectos secundarios
        return text and len(text.strip()) > 0 and len(text) <= 5000