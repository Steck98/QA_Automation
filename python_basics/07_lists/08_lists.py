# Masz:

# employees = [
#     ["Adam", "QA", 6500],
#     ["Anna", "HR", 7200],
#     ["Piotr", "Developer", 9800],
# ]

# Napisz funkcję, która:

# znajdzie pracownika "Anna",
# podniesie jej pensję o 1000 zł,
# wypisze całą listę po zmianie.


def run_employees_rise():
    employees = [
        ["Adam", "QA", 6500],
        ["Anna", "HR", 7200],
        ["Piotr", "Developer", 9800],
    ]
    pay_rise(employees)


def pay_rise(employees_list):
    for employee in employees_list:
        if employee[0] == "Anna":
            employee[2] += 1000


run_employees_rise()
