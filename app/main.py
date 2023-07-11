from fastapi import FastAPI

from app.api.routes import api_router

app = FastAPI(title= "Turing Machine TP")

app.include_router(api_router)