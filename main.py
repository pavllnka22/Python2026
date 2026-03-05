
from app.io import input
from app.io import output

def main():

    console_data = input.read_from_console()
    output.display_on_console(console_data)
    output.write_to_file_by_python(str(console_data), "data/console_output.txt")

    file_data_python= input.read_from_file("data/test.txt")
    output.display_on_console(file_data_python)
    output.write_to_file_by_python(str(file_data_python), "data/python_output.txt")

    pandas_data = input.read_from_file_by_pandas("data/test.csv")
    output.display_on_console(pandas_data)
    output.write_to_file_by_python(str(pandas_data), "data/pandas_output.txt")

if __name__ == "__main__":
    main()