# employees = [
#     {
#         "name": "Adam",
#         "position": "QA",
#         "salary": 6500,
#         "address": {
#             "city": "Gdynia",
#             "street": "Morska",
#         },
#     },
#     {
#         "name": "Anna",
#         "position": "HR",
#         "salary": 7200,
#         "address": {
#             "city": "Warszawa",
#             "street": "Puławska",
#         },
#     },
#     {
#         "name": "Piotr",
#         "position": "Developer",
#         "salary": 9800,
#         "address": {
#             "city": "Kraków",
#             "street": "Długa",
#         },
#     },
# ]
# Zadania
# 1.

# Przejdź pętlą po wszystkich pracownikach.

# Wyświetl:

# Name: Adam
# Position: QA
# Salary: 6500
# City: Gdynia
# Street: Morska
# 2.

# Znajdź pracownika:

# Anna

# Podnieś pensję o:

# 1500
# 3.

# Zmień miasto Adama na:

# Sopot
# 4.

# Dodaj do Piotra nowe pole:

# "experience": 5
# 5.

# Za pomocą get() wyświetl:

# employee.get("phone", "No phone")

# dla każdego pracownika.

# (Oczywiście nikt nie ma telefonu.)

# 6.

# Na końcu ponownie wyświetl całą bazę.


employees = [
    {
        "name": "Adam",
        "position": "QA",
        "salary": 6500,
        "address": {
            "city": "Gdynia",
            "street": "Morska",
        },
    },
    {
        "name": "Anna",
        "position": "HR",
        "salary": 7200,
        "address": {
            "city": "Warszawa",
            "street": "Puławska",
        },
    },
    {
        "name": "Piotr",
        "position": "Developer",
        "salary": 9800,
        "address": {
            "city": "Kraków",
            "street": "Długa",
        },
    },
]

for employee in employees:
    if employee["name"] == "Anna":
        print(
            f"Name: {employee['name']} \nPosition: {employee['position']} \nSalary: {employee['salary']} \nCity: {employee['address']['city']} \nStreet: {employee['address']['street']}"
        )
        employee["salary"] += 1500
    if employee["name"] == "Adam":
        employee["address"]["city"] = "sopot"
    if employee["name"] == "Piotr":
        employee.update({"experience": 5})
    print(employee.get("phone", "No phone"))
print(employees)
