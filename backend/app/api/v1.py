from fastapi import APIRouter

from app.api.endpoints import hospital
from backend.app.api.endpoints import bed, doctor, guardian, health_record, insurance, nurse, patient

api_router = APIRouter()

api_router.include_router(hospital.router, prefix="/hospitals", tags=["hospitals"])
api_router.include_router(doctor.router, prefix="/doctors", tags=["doctors"])
api_router.include_router(nurse.router, prefix="/nurses", tags=["nurses"])
api_router.include_router(patient.router, prefix="/patients", tags=["patients"])
api_router.include_router(health_record.router, prefix="/health_records", tags=["health_records"])
api_router.include_router(guardian.router, prefix="/guardians", tags=["guardians"])
api_router.include_router(insurance.router, prefix="/insurances", tags=["insurances"])
api_router.include_router(bed.router, prefix="/beds", tags=["beds"])
