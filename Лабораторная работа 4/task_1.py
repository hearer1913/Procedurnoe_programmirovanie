# TODO решите задачу
import json
FILENAME = "input.json"
def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)

    list_products = [item["score"] * item["weight"] for item in json_data]
    result = round(sum(list_products), 3)
    return result


print(task())
