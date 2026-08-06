# To jest bardzo podobne do rzeczy, które naprawdę robi się w bankowości.

# Program pobiera numer konta.

# Założenie:

# poprawny numer konta ma dokładnie 26 cyfr,
# nie może zawierać liter,
# nie może zawierać spacji,
# nie może zawierać znaków specjalnych.

account_number = input("Write your 26 digit account number")
is_number = True
if len(account_number) == 26:
    for num in account_number:
        if not num.isdigit():
            is_number = False
            print("account number is invalid")
            break
    print("account number is valid.")
else:
    print("Your account number does not contain 26 numbers, try again")
