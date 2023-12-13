"""
CI/CD
"""
import pandas as pd

def main():
    """
    Main function to execute the data processing pipeline
    """
    data = import_data()
    data = rename_columns(data)

def import_data() -> pd.DataFrame:
    """
    Import CSV file as a DataFrame
    Output: data [pd.DataFrame]
    """
    data = pd.read_csv("data/iris.csv")
    print(data.shape)  # Print the shape of the DataFrame
    return data

def rename_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns of the DataFrame
    """
    data_renamed = data.rename(columns={
        "sepal.length": 'sepal_length',
        "sepal.width": 'sepal_width',
        "petal.length": 'petal_length',
        "petal.width": 'petal_width'
    })

    return data_renamed

def data_sample(data: pd.DataFrame) -> pd.DataFrame:
    """
    Extract a sample of 50 rows from the dataset
    """
    sampled_dataframe = data.sample(50)
    return sampled_dataframe

def multiplier_dataset(data: pd.DataFrame) -> pd.DataFrame:
    """
    Multiply the sample dataset by 3

    Parameters:
        - data: The DataFrame to multiply.

    Returns:
        A DataFrame containing the multiplied dataset.
    """
    multiplied_data = pd.concat([data] * 3, ignore_index=True)
    return multiplied_data

if __name__ == '__main__':
    """
    Main entry point for script execution
    """
    main()
