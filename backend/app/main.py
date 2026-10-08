"""Turkana CIS team exercise: API.

Run from backend/:  uvicorn app.main:app --reload --port 8000
API documentation:  http://localhost:8000/docs
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.db import engine
from app.models import Base
from app.routers import alerts, datasets, health, heat, resources

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings.storage_dir.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(engine)
    yield


app = FastAPI(title="Turkana CIS team exercise", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=settings.allowed_origins, allow_methods=["*"], allow_headers=["*"])

# Every task's router is registered already, so nobody needs to edit this file to start.
app.include_router(health.router)
app.include_router(heat.router)        # Task 1
app.include_router(datasets.router)    # Task 2
app.include_router(resources.router)   # Task 3
app.include_router(alerts.router)      # Task 3
