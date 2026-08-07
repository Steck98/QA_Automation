# Masz:

# employees = [
#     ["Adam", "QA", 6500],
#     ["Anna", "HR", 7200],
#     ["Piotr", "Developer", 9800],
#     ["Karolina", "Manager", 12000],
# ]
# Zadanie

# Napisz program, który wyświetli:

# Name: Adam
# Position: QA
# Salary: 6500

# Name: Anna
# Position: HR
# Salary: 7200


def run_display_employees():
    employees = [
        ["Adam", "QA", 6500],
        ["Anna", "HR", 7200],
        ["Piotr", "Developer", 9800],
        ["Karolina", "Manager", 12000],
    ]
    display_employee(employees)


def display_employee(employees):
    for employee in employees:
        print(
            f"Name: {employee[0]} \nPosition: {employee[1]} \nSalary: {employee[2]} \n"
        )


run_display_employees()
