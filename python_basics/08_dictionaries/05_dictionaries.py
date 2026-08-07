# Firma ma bazę:

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
# ]

# Program ma mieć menu:

# 1. Show employees
# 2. Search employee
# 3. Add employee
# 4. Give raise
# 5. Exit
# 1

# Wyświetla wszystkich.

# 2

# Wyszukuje po imieniu.

# 3

# Dodaje nowego pracownika.

# Nowy słownik ma wyglądać tak:

# {
#     "name": ...,
#     "position": ...,
#     "salary": ...
# }

# i zostać dodany do listy.

# 4

# Pyta o imię.

# Jeżeli znajdzie:

# dodaje 1000 zł.

# 5

# Kończy program.


def run_employee_app():
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
    ]
    picked_option = 0
    while True:
        picked_option = display_menu()
        if picked_option == 1:
            show_employees(employees)
        elif picked_option == 2:
            search_employee(employees)
        elif picked_option == 3:
            add_employee(employees)
        elif picked_option == 4:
            give_raise(employees)
        elif picked_option == 5:
            break
    print("Thank you for using our ultra super advanced payrise system")


def display_menu():
    print(
        "1. Show employees \n2. Search employee \n3. Add employee \n4. Give raise \n5. Exit"
    )
    return int(input("What option would you like to chose? "))


def give_raise(employees_list):
    selected_employee = input("Who would you like to get a payrise? ").capitalize()
    for employee in employees_list:
        if employee["name"] == selected_employee:
            employee["salary"] += int(
                input("How much would you like to increase his salary? ")
            )


def add_employee(employees_list):
    add_name = input("What is the name of the new employee? ").capitalize()
    add_position = input("What is his role? ")
    add_salary = int(input("What will be his salary? "))
    employees_list.append(
        {"name": add_name, "position": add_position, "salary": add_salary}
    )


def search_employee(employees_list):
    searched_employee = input("Who would you like to find? ").capitalize()
    for employee in employees_list:
        if employee["name"] == searched_employee:
            print(
                f"Name: {employee['name']} \nPosition: {employee['position']} \nSalary: {employee['salary']} \n"
            )


def show_employees(employees_list):
    for employee in employees_list:
        print(
            f"Name: {employee['name']} \nPosition: {employee['position']} \nSalary: {employee['salary']} \n"
        )


run_employee_app()
