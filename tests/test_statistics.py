import numpy as np

from workstation_python.statistics.basic import descriptive_statistics


def test_descriptive_statistics():
    data = np.array([1, 2, 3, 4, 5])

    result = descriptive_statistics(data)

    assert result["mean"] == 3.0
    assert result["median"] == 3.0
    assert np.isclose(result["std"], np.sqrt(2))
    assert result["variance"] == 2.0
    assert result["q1"] == 2.0
    assert result["q3"] == 4.0
    assert result["min"] == 1.0
    assert result["max"] == 5.0
    assert result["range"] == 4.0