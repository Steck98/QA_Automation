# Zadanie — Login System

# Masz stworzyć prosty system logowania.

# Dane zapisane w systemie:

# saved_username = "Rafal"
# saved_password = "Python123"

# Użytkownik wpisuje:

# nazwę użytkownika,
# hasło.

saved_username = "Rafal"
saved_password = "Python123"

username = input("What is your ID? ")
password = input("What is your password? ")

if username == saved_username and password == saved_password:
    print("Login successful.")
else:
    if username != saved_username:
        print("Wrong username")
    if password != saved_password:
        print("Wrong password")
