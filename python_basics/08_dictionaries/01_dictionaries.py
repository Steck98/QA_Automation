# Masz słownik:

# employee = {
#     "name": "Adam",
#     "position": "QA",
#     "salary": 6500,
# }

# Napisz program który:

# Wyświetli:

# Name: Adam

# Wyświetli:

# Position: QA

# Podniesie pensję do:

# 7500

# Doda:

# "city": "Gdynia"

# Na końcu wypisze cały słownik.


def run_display_employee():
    employee = {
        "name": "Adam",
        "position": "QA",
        "salary": 6500,
    }
    print(f"Name: {employee['name']}")
    print(f"Position: {employee['position']}")
    change_employee_data(employee)


def change_employee_data(employee):
    employee["salary"] = 7000
    employee["city"] = "Gdynia"
    print(employee)


run_display_employee()
