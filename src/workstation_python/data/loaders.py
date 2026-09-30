from pathlib import Path

import pandas as pd


def _validate_file(path: str | Path) -> Path:
    """Validate that a path exists and points to a file."""
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    return path


def load_csv(path: str | Path, **kwargs) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame.

    Additional keyword arguments are forwarded to pandas.read_csv().
    """
    path = _validate_file(path)
    return pd.read_csv(path, **kwargs)


def load_tsv(path: str | Path, **kwargs) -> pd.DataFrame:
    """Load a TSV file into a pandas DataFrame.

    Additional keyword arguments are forwarded to pandas.read_csv().
    """
    path = _validate_file(path)
    return pd.read_csv(path, sep="\t", **kwargs)


def load_json(path: str | Path, **kwargs) -> pd.DataFrame:
    """Load a JSON file into a pandas DataFrame.

    Additional keyword arguments are forwarded to pandas.read_json().
    """
    path = _validate_file(path)
    return pd.read_json(path, **kwargs)