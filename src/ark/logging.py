"""A small, sane logging setup.

Uses ``rich`` for colored output when available, and falls back to the
standard library otherwise so the package never hard-depends on rich.
"""

from __future__ import annotations

import logging

from ark.config import config

_CONFIGURED = False


def _configure_root() -> None:
    global _CONFIGURED
    if _CONFIGURED:
        return

    level = getattr(logging, config.log_level.upper(), logging.INFO)
    try:
        from rich.logging import RichHandler

        handler: logging.Handler = RichHandler(rich_tracebacks=True, show_path=False)
        fmt = "%(message)s"
    except ImportError:
        handler = logging.StreamHandler()
        fmt = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"

    logging.basicConfig(level=level, format=fmt, handlers=[handler], force=True)
    _CONFIGURED = True


def get_logger(name: str = "ark") -> logging.Logger:
    """Return a configured logger. Level comes from ``config.log_level``."""
    _configure_root()
    return logging.getLogger(name)
