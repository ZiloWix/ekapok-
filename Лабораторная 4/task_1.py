import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as file:
        json_data = json.load(file)
    return round(sum([item["score"] * item["weight"] for item in json_data]), 3)


print(task())
