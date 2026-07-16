"""Reproducibility helpers.

Call :func:`set_seed` once at the start of an experiment to make Python,
NumPy, and (if installed) PyTorch deterministic.
"""

from __future__ import annotations

import os
import random


def set_seed(seed: int = 42, *, deterministic_torch: bool = True) -> int:
    """Seed all common RNGs and return the seed used.

    Seeds ``random``, ``numpy``, the ``PYTHONHASHSEED`` env var, and PyTorch
    if it is installed. Safe to call even when NumPy/PyTorch are absent.
    """
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)

    try:
        import numpy as np

        np.random.seed(seed)
    except ImportError:
        pass

    try:
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
        if deterministic_torch:
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False
    except ImportError:
        pass

    return seed
