# Bank PIN

# Bankomat działa tak:

# prosi użytkownika o wpisanie PIN-u,
# jeżeli PIN jest błędny,
# wyświetla:
# Incorrect PIN. Try again.

# i pyta ponownie.

# Jeżeli PIN jest poprawny:

# Access granted.

# i kończy działanie programu.

# Załóż:

# correct_pin = "1234"

# Nie ma jeszcze limitu prób.

# Program ma pytać tak długo, aż użytkownik poda poprawny PIN.
correct_pin = "1234"
user_pin = ""

user_pin = input("Write your pin ")
while user_pin != correct_pin:
    print("Incorrect PIN. Try again.")
    user_pin = input("Write the correct pin ")

print("Access granted. ")
