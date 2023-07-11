from fastapi import APIRouter

from app.services import mtu

api_router = APIRouter()

api_router.include_router(mtu.router, prefix="", tags=["Turing Machine"])