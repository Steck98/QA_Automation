# Masz:

# employees = [
#     "Adam",
#     "Jan",
#     "Anna",
#     "Piotr",
#     "Karolina",
# ]

# Program ma:

# Zapytać użytkownika o imię pracownika.
# Sprawdzić, czy taki pracownik istnieje.
# Jeżeli istnieje:
# Employee found.
# Jeżeli nie:
# Employee not found.

# Nie używaj:

# in

# Chcę, żebyś sam przeszedł pętlą po liście.

# To jest bardzo ważne ćwiczenie.

# Możesz użyć:

# for
# if
# bool
# break


def run_all_employees():
    employees = [
        "Adam",
        "Jan",
        "Anna",
        "Piotr",
        "Karolina",
    ]
    if check_employee(employees):
        print("Employee found.")
    else:
        print("Employee not found.")


def check_employee(employees_list):
    searched_employee = input("Who are we looking for ? ").capitalize()
    for employee in employees_list:
        if searched_employee == employee:
            return True
    return False


run_all_employees()
