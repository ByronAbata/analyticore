#!/usr/bin/env python3
"""
Script para inicializar la base de datos en Render
"""
from database import engine, Base
from app.models.job_mod import Job

def init_database():
    """Crear todas las tablas en la base de datos"""
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Base de datos inicializada correctamente")
    except Exception as e:
        print(f"❌ Error inicializando base de datos: {e}")
        raise e

if __name__ == "__main__":
    init_database() 