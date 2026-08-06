# Masz listę:

# employees = [
#     "Adam",
#     "Jan",
#     "Anna",
#     "Piotr",
#     "Karolina",
# ]

# Napisz program, który:

# Wypisze wszystkich pracowników.
# Przy każdym pracowniku wypisze numer:

# Przykład:

# Employee #1: Adam
# Employee #2: Jan
# Employee #3: Anna
# Employee #4: Piotr
# Employee #5: Karolina
# Warunki
# Nie używaj range().
# Nie używaj enumerate().
# Nie używaj gotowych funkcji poza len().

# Masisz zrobić to tylko z użyciem:

# for
# listy
# zmiennej pomocniczej


def run_all_employees():
    employees = [
        "Adam",
        "Jan",
        "Anna",
        "Piotr",
        "Karolina",
    ]
    print_employees_list(employees)


def print_employees_list(employees):
    i = 0
    for employee in employees:
        i += 1
        print(f"#{i}: {employee}")
    print(f"Total employees: {len(employees)}")


run_all_employees()
