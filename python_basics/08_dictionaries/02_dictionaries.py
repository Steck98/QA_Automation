# Zadanie:

# employees = [
#     {
#         "name": "Adam",
#         "position": "QA",
#         "salary": 6500,
#     },
#     {
#         "name": "Anna",
#         "position": "HR",
#         "salary": 7200,
#     },
#     {
#         "name": "Piotr",
#         "position": "Developer",
#         "salary": 9800,
#     },
# ]

# Napisz program, który:

# Wypisze wszystkich pracowników.
# Dla każdego wyświetli:
# Name: Adam
# Position: QA
# Salary: 6500

# Na końcu znajdzie pracownika "Anna" i zwiększy jej pensję o 1000 zł.
# Ponownie wyświetli całą listę.


def run_employees_list():
    employees = [
        {
            "name": "Adam",
            "position": "QA",
            "salary": 6500,
        },
        {
            "name": "Anna",
            "position": "HR",
            "salary": 7200,
        },
        {
            "name": "Piotr",
            "position": "Developer",
            "salary": 9800,
        },
    ]
    display_employee(employees)
    employee_pay_rise(employees)
    display_employee(employees)


def display_employee(employees_list):
    for employee in employees_list:
        print(
            f"Name: {employee['name']} \nPosition: {employee['position']} \nSalary: {employee['salary']}"
        )


def employee_pay_rise(employees_list):
    for employee in employees_list:
        if employee["name"] == "Anna":
            employee["salary"] += 1000


run_employees_list()
