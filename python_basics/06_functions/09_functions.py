# Bank podejmuje decyzję o przyznaniu kredytu.

# Dane od użytkownika:

# miesięczny dochód,
# miesięczne wydatki,
# liczba lat zatrudnienia,
# czy klient ma zaległości w BIK (yes/no).
# Zasady

# Kredyt można przyznać tylko wtedy, gdy:

# dochód jest większy od wydatków,
# klient pracuje minimum 2 lata,
# nie ma zaległości w BIK.
# Wynik

# Jeżeli wszystko jest OK:

# Loan approved.

# Jeżeli nie:

# Loan denied.

# oraz wszystkie powody odmowy, np.:

# Reason: income is too low.
# Reason: employment period is too short.
# Reason: active debt found.
# Jeżeli:

# income - expenses >= 5000

# to oprócz:

# Loan approved.

# ma się pojawić:

# Preferred customer.


def initiate_loan():
    monthly_wage = int(input("What is your monthly wage? "))
    monthly_expenses = int(input("What are your monthly expenses? "))
    years_of_work = int(input("How many years have you been working? "))
    has_arrears = input("Do you have any arrears? yes/no").lower()
    if client_validation(monthly_wage, monthly_expenses, years_of_work, has_arrears):
        print("Loan approved.")
        if has_client_vip(monthly_wage, monthly_expenses):
            print("Preferred customer.")


def client_validation(wage, expenses, working_years, arrears):
    if wage <= expenses:
        print("Reason: income is too low")
    if working_years < 2:
        print("Reason: employment period is too short.")
    if arrears == "yes":
        print("Reason: active debt found.")
    return wage > expenses and working_years >= 2 and arrears == "no"


def has_client_vip(income, expenses):
    return income - expenses >= 5000


initiate_loan()
