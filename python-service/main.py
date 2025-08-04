from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.job_controller import router as job_router
from database import engine, Base
from app.models.job_mod import Job

# Initialize database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AnalytiCore API", version="1.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(job_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "AnalytiCore API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 