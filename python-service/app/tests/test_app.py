from fastapi.testclient import TestClient
from app import create_app

client = TestClient(create_app())

def test_submit_job_success():
    response = client.post("/submit", json={"text": "Este es un texto válido"})
    assert response.status_code == 200
    assert "jobId" in response.json()

def test_submit_job_invalid():
    response = client.post("/submit", json={"text": ""})
    assert response.status_code == 400
