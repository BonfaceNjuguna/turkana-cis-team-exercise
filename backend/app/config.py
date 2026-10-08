"""Settings, read from environment variables or backend/.env (see .env.example)."""
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parents[1]
REPO_DIR = BACKEND_DIR.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BACKEND_DIR / ".env", extra="ignore")

    database_url: str = f"sqlite:///{BACKEND_DIR / 'cis_exercise.db'}"
    # Uploaded files (Task 2). Created on start-up; ignored by Git.
    storage_dir: Path = BACKEND_DIR / "storage"
    # Sub-counties and main towns with coordinates (Task 1 and Task 3).
    places_file: Path = REPO_DIR / "data" / "turkana_places.json"
    allowed_origins: list[str] = ["http://localhost:5173"]


@lru_cache
def get_settings() -> Settings:
    return Settings()
