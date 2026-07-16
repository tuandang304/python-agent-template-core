"""Agent Research Kit (ark) — a reproducible research project package.

Import the pieces you need:

    from ark import config, set_seed, get_logger
"""

from ark.config import DATA_DIR, PROJECT_ROOT, RESULTS_DIR, config
from ark.logging import get_logger
from ark.seed import set_seed

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "config",
    "PROJECT_ROOT",
    "DATA_DIR",
    "RESULTS_DIR",
    "get_logger",
    "set_seed",
]
