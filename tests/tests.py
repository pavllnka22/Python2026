
import os
import pandas
from app.io.input import read_from_file, read_from_file_by_pandas


def test_read_file_builtin_success():

    file_name = "temp_test.txt"
    content = "Test content for builtin"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)

    result = read_from_file(file_name)
    os.remove(file_name)
    assert result == content


def test_read_file_builtin_not_found():

    result = read_from_file("non_existent_file.txt")
    assert "Error" in result


def test_read_file_builtin_empty():

    file_name = "empty_test.txt"
    open(file_name, 'a').close()

    result = read_from_file(file_name)
    os.remove(file_name)
    assert result == ""


def test_read_file_pandas_returns_dataframe():

    file_name = "temp_test.csv"
    df_original = pandas.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    df_original.to_csv(file_name, index=False)

    result = read_from_file_by_pandas(file_name)
    os.remove(file_name)
    assert isinstance(result, pandas.DataFrame)
    assert result.shape == (2, 2)


def test_read_file_pandas_content_check():

    file_name = "content_test.csv"
    with open(file_name, "w") as f:
        f.write("a,b\n10,20")

    result = read_from_file_by_pandas(file_name)
    os.remove(file_name)
    assert result["a"][0] == 10


def test_read_file_pandas_error_handling():

    result = read_from_file_by_pandas("missing_file.csv")
    assert "Pandas Error" in result