"""
Tests
"""
from run import import_data, rename_columns, data_sample

def test_import_data():
    """
    Test import_data function
    """
    data = import_data()
    assert data.shape[0] > 0

def test_rename_columns():
    """
    Test rename_columns function
    """
    data = import_data()
    data_renamed = rename_columns(data)
    assert "sepal_length" in data_renamed.columns

def test_data_sample():
    """
    Test data_sample function
    """
    data = import_data()
    echantillon = data_sample(data)
    expected_length = 50
    assert len(echantillon) == expected_length, f"Expected the sample size to be {expected_length}, but it is {len(echantillon)}."
    print("All tests passed successfully.")
