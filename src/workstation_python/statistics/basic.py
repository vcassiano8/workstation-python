import numpy as np


def descriptive_statistics(data: np.ndarray) -> dict[str, float]:
    """Calculate basic descriptive statistics."""
    if data.size == 0:
        raise ValueError("Data cannot be empty.")

    return {
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "std": float(np.std(data)),
        "variance": float(np.var(data)),
        "q1": float(np.percentile(data, 25)),
        "q3": float(np.percentile(data, 75)),
        "min": float(np.min(data)),
        "max": float(np.max(data)),
        "range": float(np.max(data) - np.min(data)),
    }