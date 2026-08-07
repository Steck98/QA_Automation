# Masz:

# employee = {
#     "name": "Adam",
#     "position": "QA",
# }

# Napisz program, który wyświetli:

# imię,
# stanowisko,
# miasto.

# Ale miasto pobierz przez get() i ustaw domyślną wartość:

# Unknown


def run_display_employee():
    employee = {
        "name": "Adam",
        "position": "QA",
    }
    display_employee(employee)


def display_employee(employee):
    print(
        f"Name: {employee['name']} \nPosition: {employee['position']} \nCity: {employee.get('city', 'Unknown')}"
    )


run_display_employee()
