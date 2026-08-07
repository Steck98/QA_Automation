# Firma ma bazę.

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
# Zadanie

# Napisz mini system wyszukiwania.

# Program pyta:

# Employee name:

# Na przykład:

# Anna

# Jeżeli pracownik istnieje:

# Wyświetl:

# Name: Anna
# Position: HR
# Salary: 7200

# Jeżeli nie istnieje:

# Employee not found.
# Warunki
# funkcje,
# pętla,
# słowniki,
# możesz użyć return,


def run_employee_search():
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
    if not search_employee(employees):
        print("Employee not found.")


def search_employee(employees_list):
    searched_employee = input("Who are you looking for? ").capitalize()
    for employee in employees_list:
        if employee["name"] == searched_employee:
            print(
                f"Name: {employee['name']} \nPosition: {employee['position']} \nSalary: {employee['salary']}"
            )
            return True


run_employee_search()
