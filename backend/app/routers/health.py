"""A working example endpoint: GET /api/health."""
from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db import get_db
from app.places import load_places

router = APIRouter(prefix="/api", tags=["health"])


@router.get("/health")
def health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))  # proves the database is reachable
    return {
        "status": "ok",
        "time": datetime.now(timezone.utc).isoformat(),
        "places": len(load_places()["places"]),
    }
