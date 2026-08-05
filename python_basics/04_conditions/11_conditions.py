# Program pobiera:

# Username
# Password
# Is account active? (yes/no)
# Is email verified? (yes/no)
# Failed login attempts

# Dane zapisane w systemie:

# saved_username = "Rafal"
# saved_password = "Python123"
# maximum_failed_attempts = 3

# Program ma działać według tych zasad:

# Jeżeli konto jest nieaktywne:
# Access denied: account is inactive.
# Jeżeli liczba nieudanych prób wynosi co najmniej 3:
# Access denied: account is locked.
# Jeżeli konto działa, ale e-mail nie jest zweryfikowany:
# Access denied: email is not verified.
# Jeżeli login albo hasło są niepoprawne, wypisz wszystkie odpowiednie komunikaty:
# Incorrect username.
# Incorrect password.
# Dostęp zostaje przyznany wyłącznie wtedy, gdy wszystkie wymagania są spełnione:
# Login successful.
# Ważna zasada kolejności

# Zablokowane lub nieaktywne konto nie powinno przechodzić do sprawdzania danych logowania. Najpierw sprawdź stan konta, a dopiero potem login i hasło.

saved_username = "Rafal"
saved_password = "Python123"
maximum_failed_attempts = 3

username = input("What is your ID? ")
password = input("What is your password? ")
active_account = input("Is your account Active ? yes/no ")
verified_mail = input("Is you email verified? yes/no ")
failed_login_attempts = int(input("How many times you failed to log in ? "))

if active_account == "yes" and failed_login_attempts < maximum_failed_attempts:
    print("Account is Valid")
    if verified_mail == "yes":
        print("mail is verified")
        if username == saved_username and password == saved_password:
            print("Login successful.")
        else:
            if username != saved_username:
                print("Incorrect username.")
            if password != saved_password:
                print("Incorrect password.")
    else:
        print("Access denied: email is not verified.")
else:
    if active_account == "no":
        print("Access denied: account is inactive.")
    if failed_login_attempts >= maximum_failed_attempts:
        print("Access denied: account is locked.")
