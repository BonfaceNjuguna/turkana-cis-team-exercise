"""Test setup: every test gets an empty database and storage folder of its own.

Use the `client` fixture to call the API:

    def test_something(client):
        response = client.get("/api/health")
        assert response.status_code == 200
"""
import os
import tempfile
from pathlib import Path

import pytest

# Point the app at a throwaway database and storage folder before it is imported.
_tmp = tempfile.mkdtemp(prefix="cis-exercise-tests-")
os.environ["DATABASE_URL"] = f"sqlite:///{Path(_tmp) / 'test.db'}"
os.environ["STORAGE_DIR"] = str(Path(_tmp) / "storage")

from fastapi.testclient import TestClient  # noqa: E402

from app.config import get_settings  # noqa: E402
from app.db import engine  # noqa: E402
from app.main import app  # noqa: E402
from app.models import Base  # noqa: E402

SAMPLES = Path(__file__).resolve().parents[2] / "data" / "samples"


@pytest.fixture
def client():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    storage = get_settings().storage_dir
    storage.mkdir(parents=True, exist_ok=True)
    for f in storage.iterdir():
        if f.is_file():
            f.unlink()
    with TestClient(app) as c:
        yield c


@pytest.fixture
def samples() -> Path:
    """The folder data/samples, for upload tests (Task 2)."""
    return SAMPLES
