"""Turkana's sub-counties and main towns, from data/turkana_places.json."""
import json
from functools import lru_cache

from app.config import get_settings


@lru_cache
def load_places() -> dict:
    """{"sub_counties": [...], "places": [{"id", "name", "sub_county", "kind", "lat", "lon"}, ...]}"""
    return json.loads(get_settings().places_file.read_text(encoding="utf-8"))
