import numpy as np
import pytest

from workstation_python.statistics.inferential import pearson_correlation


def test_pearson_correlation_positive():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])

    result = pearson_correlation(x, y)

    assert np.isclose(result["correlation"], 1.0)
    assert result["p_value"] < 0.05


def test_pearson_correlation_empty_array():
    x = np.array([])
    y = np.array([])

    with pytest.raises(ValueError, match="Input arrays cannot be empty."):
        pearson_correlation(x, y)


def test_pearson_correlation_different_sizes():
    x = np.array([1, 2, 3])
    y = np.array([1, 2])

    with pytest.raises(ValueError, match="Input arrays must have the same size."):
        pearson_correlation(x, y)


def test_pearson_correlation_too_few_observations():
    x = np.array([1])
    y = np.array([2])

    with pytest.raises(ValueError, match="At least two observations are required."):
        pearson_correlation(x, y)