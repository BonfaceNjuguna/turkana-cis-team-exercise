"""Task 3: resources. See docs/tasks/3-resources-and-alerts.md.

Suggested endpoints: GET/POST /api/resources, GET/PATCH/DELETE /api/resources/{id}, POST /api/resources/{id}/publish
"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/resources", tags=["Task 3: resources"])
