employee = {
    "name": "Adam",
    "position": "QA",
    "salary": 6500,
}

for key, value in employee.items():
    print(f"{key}: {value}")

if "city" in employee:
    print("key exist")
else:
    print("City not found.")

employee.update({"city": "Gdynia"})
employee.get("city")
employee.get("phone", "Unknown")
employee.update({"salary": 7500, "experience": 3})

for key, value in employee.items():
    print(f"{key}: {value}")

employee.pop("experience")
print(len(employee))

print(employee)

employee_copy = employee.copy()

employee_copy["name"] = "Anna"
print(employee)
print(employee_copy)
