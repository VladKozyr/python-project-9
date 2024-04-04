import pandas as pd


def input_text() -> str:
    """
    Function to input text from the console.

    Returns:
        str: The text entered by the user from the console.
    """
    return input("Enter text: ")


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
    try:
        with open(path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."


def read_file_pandas(path: str) -> pd.DataFrame | None:
    """
    Function to read content from a file using the pandas library.

    Args:
        path (str): File path

    Returns:
        pandas.DataFrame: The content read from the file as a DataFrame.

    Raises:
        FileNotFoundError - If the file does not exist
    """
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        return None
