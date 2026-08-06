# W wielu firmach obowiązuje polityka haseł.

# Napisz program, który sprawdzi, czy hasło spełnia następujące wymagania:

# minimum 8 znaków,
# zawiera co najmniej jedną cyfrę,
# zawiera co najmniej jedną wielką literę,
# zawiera co najmniej jedną małą literę.

user_password = input(
    "Your password must contain one upper and lower case and one number "
)
has_required_length = len(user_password) >= 8
has_number = False
has_uppercase = False
has_lowercase = False

for char in user_password:
    if char.isdigit():
        has_number = True
        print(char)
    if char.isupper():
        has_uppercase = True
        print(char)
    if char.islower():
        has_lowercase = True
        print(char)
if has_required_length and has_uppercase and has_lowercase and has_number:
    print("Password is Valid")
else:
    print("Invalid Password try again")
