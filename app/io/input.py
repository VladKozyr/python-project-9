import pandas as pd


def input_text() -> str:
    """
    Function to input text from the console.

    Returns:
        str: The text entered by the user from the console.
    """
    pass


def read_file(path: str) -> str:
    """
    Function to read content from a file using built-in Python capabilities.

    Args:
        path (str): File path

    Returns:
        str: The content read from the file.

    Raises:
        FileNotFoundError - If the file does not exist
    """
    pass


def read_file_pandas(path: str) -> pd.DataFrame:
    """
    Function to read content from a file using the pandas library.

    Args:
        path (str): File path

    Returns:
        pandas.DataFrame: The content read from the file as a DataFrame.

    Raises:
        FileNotFoundError - If the file does not exist
    """
    pass
