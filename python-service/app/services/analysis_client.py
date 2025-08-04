import os
import requests
import asyncio
from app.models.job_mod import JobStatus

class AnalysisClient:
    def __init__(self):
        self.base_url = os.getenv("JAVA_SERVICE_URL", "http://localhost:8080")

    def start_analysis(self, job_id: str):
        try:
            response = requests.post(
                f"{self.base_url}/analizar", 
                json={"jobId": job_id},
                timeout=30
            )
            if response.status_code == 200:
                print(f"[INFO] Análisis iniciado para job {job_id}")
            else:
                print(f"[ERROR] Error al iniciar análisis: {response.status_code}")
        except Exception as e:
            print(f"[ERROR] No se pudo contactar con el servicio Java: {e}")

    async def start_analysis_async(self, job_id: str):
        """Versión asíncrona para mejor manejo de errores"""
        try:
            async with asyncio.timeout(30):
                # Aquí podrías usar aiohttp para llamadas asíncronas
                response = requests.post(
                    f"{self.base_url}/analizar", 
                    json={"jobId": job_id}
                )
                return response.status_code == 200
        except Exception as e:
            print(f"[ERROR] Error asíncrono: {e}")
            return False
