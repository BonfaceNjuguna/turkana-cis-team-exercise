"""Task 2: datasets. See docs/tasks/2-datasets.md.

Suggested endpoints: POST/GET /api/datasets, GET/PATCH/DELETE /api/datasets/{id}, GET /api/datasets/{id}/download
Store uploaded files in get_settings().storage_dir.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/datasets", tags=["Task 2: datasets"])
