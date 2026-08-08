import json

with open("python_basics/10_json/employee.json") as file:
    data = json.load(file)
    print(data["name"])
    print(data)
