import csv
from tp1.ejercicio7 import convert


def test_e7():
    convert("tp1/tests/MOCK_DATA.csv", "tp1/tests/MOCK_DATA_r.csv")

    with open(
        "tp1/tests/MOCK_DATA_r.csv", "r", newline="", encoding="utf-8"
    ) as f, open(
        "tp1/tests/MOCK_DATA_RESULT.csv", "r", newline="", encoding="utf-8"
    ) as f2:
        content_file1 = csv.reader(f)
        content_file2 = csv.reader(f2)

        data_file1 = [row for row in content_file1]
        data_file2 = [row for row in content_file2]

        for f1, f2 in zip(data_file1, data_file2):
            if f1 == f2:
                print(f"id {f1[0]} - OK")
            else:
                print(f"id {f1[0]} - ERROR")


def run_tests_tp1_ej7():
    test_e7()
