from app.models.job_mod import Job
from datetime import datetime

class JobRepository:
    def __init__(self, db):
        self.db = db

    def save(self, job: Job):
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job

    def update(self, job: Job):
        job.updated_at = datetime.utcnow()
        self.db.commit()
        self.db.refresh(job)
        return job

    def find_by_job_id(self, job_id: str):
        return self.db.query(Job).filter(Job.job_id == job_id).first()
