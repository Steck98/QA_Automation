# Napisz funkcję:

# can_withdraw(balance, amount)

# Ma zwrócić:

# True, jeśli balance >= amount,
# False, jeśli nie.

# Potem użyj jej tak:

# if can_withdraw(1000, 300):
#     print("Withdrawal approved.")
# else:
#     print("Insufficient funds.")


def can_withdraw(balance, amount):
    return balance >= amount


if can_withdraw(1000, 300):
    print("Withdrawal approved.")
else:
    print("Insufficient funds.")
