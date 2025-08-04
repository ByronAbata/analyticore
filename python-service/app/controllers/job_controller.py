from fastapi import APIRouter, Request, HTTPException
from database import SessionLocal
from app.repositories.job_rep import JobRepository
from app.services.job_service import JobService
from app.services.analysis_client import AnalysisClient
from app.models.job_mod import Job

router = APIRouter()

@router.post("/submit")
async def submit_text(request: Request):
    data = await request.json()
    text = data.get("text", "")
    db = SessionLocal()
    service = JobService(JobRepository(db), AnalysisClient())
    try:
        job_id = service.submit_job(text)
        return {"jobId": job_id, "status": "PENDING"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/status/{job_id}")
def get_status(job_id: str):
    db = SessionLocal()
    service = JobService(JobRepository(db), AnalysisClient())
    try:
        return service.get_job_status(job_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
