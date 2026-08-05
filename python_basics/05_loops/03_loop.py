# Piszesz prosty program bankomatu.

# Na koncie użytkownika znajduje się:

# account_balance = 2500

# Program działa w pętli.

# Za każdym razem pyta:

# How much money would you like to withdraw?
# Zasady

# Jeżeli użytkownik wpisze:

# 1. Kwotę większą od salda

# Wyświetl:

# Insufficient funds.

# i zapytaj ponownie.

# 2. Liczbę mniejszą lub równą 0

# Wyświetl:

# Invalid amount.

# i zapytaj ponownie.

# 3. Poprawną kwotę

# Odejmij ją od salda.

# Wyświetl:

# Withdrawal successful.
# Remaining balance: ...

# Następnie zakończ program.

account_balance = 2500
withdrawal_complete = False

while withdrawal_complete == False:
    withdrawal_amount = int(input("How much would you like to withdrawal? "))
    if withdrawal_amount > account_balance:
        print("Insufficient funds.")
    if withdrawal_amount <= 0:
        print("Invalid amount.")
    if withdrawal_amount > 0 and withdrawal_amount <= account_balance:
        account_balance -= withdrawal_amount
        print(f"Withdrawal successful. \nRemaining balance: {account_balance}")
        withdrawal_complete = True
