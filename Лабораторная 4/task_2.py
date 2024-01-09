import csv
import json
from collections import OrderedDict


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as input_file:
        cvs_data = csv.DictReader(input_file, delimiter=",")
        list_csv = [line for line in cvs_data]

    with open(OUTPUT_FILENAME, "w") as output_file:
        output_file.write(json.dumps(list_csv, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
