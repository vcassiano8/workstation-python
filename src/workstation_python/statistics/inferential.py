import numpy as np
from scipy import stats


def pearson_correlation(
    x: np.ndarray,
    y: np.ndarray,
) -> dict[str, float]:
    """Calculate Pearson's correlation coefficient and p-value."""
    if x.size == 0 or y.size == 0:
        raise ValueError("Input arrays cannot be empty.")

    if x.size != y.size:
        raise ValueError("Input arrays must have the same size.")

    if x.size < 2:
        raise ValueError("At least two observations are required.")

    result = stats.pearsonr(x, y)

    return {
        "correlation": float(result.statistic),
        "p_value": float(result.pvalue),
    }