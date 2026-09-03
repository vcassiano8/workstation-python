import pandas as pd
import pytest

from workstation_python.data.loaders import load_csv, load_tsv


def test_load_csv(tmp_path):
    csv_file = tmp_path / "data.csv"
    csv_file.write_text("name,value\nA,10\nB,20\n")

    dataframe = load_csv(csv_file)

    assert isinstance(dataframe, pd.DataFrame)
    assert list(dataframe.columns) == ["name", "value"]
    assert dataframe["value"].tolist() == [10, 20]


def test_load_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_csv("data/nonexistent.csv")


def test_load_csv_path_is_directory(tmp_path):
    with pytest.raises(ValueError):
        load_csv(tmp_path)


def test_load_tsv(tmp_path):
    tsv_file = tmp_path / "data.tsv"
    tsv_file.write_text("name\tvalue\nA\t10\nB\t20\n")

    dataframe = load_tsv(tsv_file)

    assert isinstance(dataframe, pd.DataFrame)
    assert list(dataframe.columns) == ["name", "value"]
    assert dataframe["value"].tolist() == [10, 20]
