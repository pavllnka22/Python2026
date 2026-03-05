def display_on_console(data):
    """
     Displays data entered to console.
     Args:
      data (any): data to display(string, number etc)

    """
    print("\n--- Entered data ---")
    print(data)
    print("------------------------\n")


def write_to_file_by_python(data, file_path):
    """
            Writes data entered to file by python.

            Args:
                data (str): data to write.
                file_path (str): path to file.
    """
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(str(data) + "\n")
    print(f"Successfully saved to  {file_path}")
