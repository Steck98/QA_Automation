# Napisz funkcję:

# calculate_interest(balance)

# Założenie:

# Bank daje 5% odsetek.

# Czyli:

# 1000

# ↓

# funkcja ma zwrócić:

# 50


def calculate_interest(balance):
    return balance / 100 * 5


interest = calculate_interest(1000)
print(f"Interest: {interest}")
