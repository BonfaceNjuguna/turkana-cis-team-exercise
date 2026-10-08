"""Task 1: heat map. See docs/tasks/1-heat-map.md.

Suggested endpoint: GET /api/heat/forecast
The places are in app.places.load_places().
"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/heat", tags=["Task 1: heat map"])
