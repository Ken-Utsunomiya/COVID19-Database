from fastapi import APIRouter

from app.api.endpoints import hospital

api_router = APIRouter()

api_router.include_router(hospital.router, prefix="/hospitals", tags=["hospitals"])
