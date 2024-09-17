import pytest
from app.main import read_csv_file

def test_read_csv_file():
    test_file_path = 'tests/test_data.csv'
    expected_columns = ["id", "name", "value"]
    expected_row_count = 3

    df = read_csv_file(test_file_path)

    assert list(df.columns) == expected_columns
    assert len(df) == expected_row_count
    assert df.iloc[0]["id"] == 1
    assert df.iloc[0]["name"] == "Item 1"
    assert df.iloc[0]["value"] == 100.0
    