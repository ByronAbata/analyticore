from app.models.job_mod import Job, JobStatus
import json

class JobService:
    def __init__(self, job_repository, analysis_client):
        self.job_repository = job_repository
        self.analysis_client = analysis_client
    
    def submit_job(self, text_content: str) -> str:
        # Función pura para validación
        if not self._is_valid_text(text_content):
            raise ValueError("Invalid text content")
        
        job = Job(text_content=text_content, status=JobStatus.PENDING)
        self.job_repository.save(job)
        
        # Llamada síncrona al servicio Java
        try:
            self.analysis_client.start_analysis(job.job_id)
            # Actualizar estado a PROCESSING
            job.status = JobStatus.PROCESSING
            self.job_repository.update(job)
        except Exception as e:
            job.status = JobStatus.FAILED
            self.job_repository.update(job)
            raise e
        
        return job.job_id
    
    def get_job_status(self, job_id: str) -> dict:
        job = self.job_repository.find_by_job_id(job_id)
        if not job:
            raise ValueError("Job not found")
        
        return {
            "jobId": job.job_id,
            "status": job.status,
            "sentiment_score": float(job.sentiment_score) if job.sentiment_score else None,
            "keywords": job.keywords or [],
            "created_at": job.created_at,
            "updated_at": job.updated_at,
        }
    
    def _is_valid_text(self, text: str) -> bool:
        # Función pura - mismo input, mismo output, sin efectos secundarios
        return text and len(text.strip()) > 0 and len(text) <= 5000
