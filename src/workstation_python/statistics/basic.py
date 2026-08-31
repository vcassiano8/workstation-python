import numpy as np


def descriptive_statistics(data: np.ndarray) -> dict[str, float]:
    """Calculate basic descriptive statistics."""
    return {
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "std": float(np.std(data)),
        "min": float(np.min(data)),
        "max": float(np.max(data)),
    }