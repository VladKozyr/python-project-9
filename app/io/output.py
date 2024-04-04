def output_console(text: str):
    """
    Function to print text to the console.

    Args:
        text (str): The text to be printed to the console.

    Returns:
        None
    """
    print(text)


def write_file(path: str, content: str):
    """
    Function to write content to a file.

    Args:
        path (str): The path to the file to write
        content (str): The content to write to the file

    Returns:
        None

    Raises:
        FileNotFoundError: If the file does not exist
        IOError - If the file does not exist or some IO error happen
    """
    with open(path, 'w') as file:
        file.write(content)
