import pandas


def read_from_console():
    """
       Reads data from console.

        Returns:
            str: data entered by the user.
    """
    return input("Enter data: ")


def read_from_file(file_path):
    """
        Reads data from file.

        Args:
            file_path (str): path to file.

        Returns:
            str: data from file.
        """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: file {file_path} not found."


def read_from_file_by_pandas(file_path):
    """
            Reads data from file using Pandas library.

            Args:
                file_path (str): path to file.

            Returns:
                str: data from file.
            """
    try:
        df = pandas.read_csv(file_path)
        return df
    except Exception as e:
        return f"Pandas error: {e}"