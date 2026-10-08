"""Task 3: alerts. See docs/tasks/3-resources-and-alerts.md.

Suggested endpoints: GET/POST /api/alerts, GET/PATCH/DELETE /api/alerts/{id},
POST /api/alerts/{id}/publish, POST /api/alerts/{id}/withdraw
"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/alerts", tags=["Task 3: alerts"])
