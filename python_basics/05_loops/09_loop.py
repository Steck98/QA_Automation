# Password Analyzer

# Program pobiera hasło od użytkownika.

# Ma policzyć:

# ile znaków ma hasło.

# Na końcu wyświetla:

# Password length: 12
# Ograniczenia

# ⚠️ Nie używaj:

# len()

user_password = input("What is your password? ")
i = 0
for letter in user_password:
    i += 1
print(f"Password length: {i}")
