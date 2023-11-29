"""
CI/CD
"""
import pandas as pd

def main():
    """
    Main
    """
    import_data()

def import_data():
    data=pd.read_csv("data/iris.csv")
    print(data.shape)
    return data


if __name__ == '__main__':
    """
    Doc
    """
    main()