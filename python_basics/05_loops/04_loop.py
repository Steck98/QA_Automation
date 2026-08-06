# Program zaczyna z saldem:

# account_balance = 2500

# Następnie wyświetla menu:

# ===== BANK MENU =====
# 1. Check balance
# 2. Deposit money
# 3. Withdraw money
# 4. Exit

# Program ma działać w pętli tak długo, aż użytkownik wybierze 4.

# Zasady

# 1 — Check balance

# Wyświetl aktualne saldo:

# Current balance: 2500

# 2 — Deposit money

# Zapytaj o kwotę wpłaty.

# kwota musi być większa od 0,
# jeśli jest poprawna, dodaj ją do salda,
# jeśli nie, wyświetl:
# Invalid amount.

# 3 — Withdraw money

# Zapytaj o kwotę wypłaty.

# kwota musi być większa od 0,
# nie może być większa od salda,
# po poprawnej wypłacie odejmij ją od salda,
# przy błędzie pokaż właściwy komunikat.

# 4 — Exit

# Wyświetl:

# Thank you for using our bank.

# i zakończ program.


def run_bank():
    account_balance = 2500
    user_choice = 0
    while user_choice != 4:
        user_choice = show_menu()

        if user_choice == 1:
            check_balance(account_balance)
        elif user_choice == 2:
            account_balance = deposit_money(account_balance)
        elif user_choice == 3:
            account_balance = withdraw_money(account_balance)
        elif user_choice == 4:
            print("Thank you for using our bank.")
        else:
            print("Invalid option.")


def show_menu():
    return int(
        input("1. Check balance \n2. Deposit money \n3. Withdraw money \n4. Exit")
    )


def check_balance(account_balance):
    print(f"Current balance: {account_balance}")


def deposit_money(account_balance):
    deposit_amount = int(input("How much would you like to deposit? "))
    if deposit_amount > 0:
        return account_balance + deposit_amount
    print("Invalid amount.")
    return account_balance


def withdraw_money(account_balance):
    withdrawal_amount = int(input("How much would you like to withdraw? "))
    if withdrawal_amount > 0 and withdrawal_amount <= account_balance:
        return account_balance - withdrawal_amount
    print("Invalid amount.")
    return account_balance


run_bank()
