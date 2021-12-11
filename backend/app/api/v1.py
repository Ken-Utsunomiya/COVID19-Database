from fastapi import APIRouter

from app.api.endpoints import hospital
from backend.app.api.endpoints import doctor, nurse

api_router = APIRouter()

api_router.include_router(hospital.router, prefix="/hospitals", tags=["hospitals"])
api_router.include_router(doctor.router, prefix="/doctors", tags=["doctors"])
api_router.include_router(nurse.router, prefix="/nurses", tags=["nurses"])
