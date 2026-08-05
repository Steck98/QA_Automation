# Password Policy

# Program pobiera hasło.

# Ma policzyć:

# ile zawiera cyfr.

# Przykład:

# Python12345

# ↓

# Digits found: 5
# Ograniczenia

# Nie używaj:

# isdigit()
# count()
# regex
# len()

# 💡 Ma Ci wystarczyć to, co już znasz.

user_password = input("What is your password? ")
digits_found = 0
digits = "0123456789"
for letter in user_password:
    if letter in digits:
        digits_found += 1


print(digits_found)
