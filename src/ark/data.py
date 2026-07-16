"""Tiny data-IO helpers built on the standard project paths.

These are conveniences, not a framework — read them, then adapt to your data.
"""

from __future__ import annotations

from pathlib import Path

from ark.config import PROCESSED_DATA_DIR, RAW_DATA_DIR


def raw(name: str) -> Path:
    """Return the path to a file in ``data/raw/``."""
    return RAW_DATA_DIR / name


def processed(name: str) -> Path:
    """Return the path to a file in ``data/processed/`` (parents created)."""
    path = PROCESSED_DATA_DIR / name
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
