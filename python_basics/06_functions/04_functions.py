# Bank pobiera prowizję od przelewu.

# Napisz funkcję:

# calculate_transfer_fee(amount)

# Zasady:

# do 1000 zł → prowizja 5 zł
# powyżej 1000 zł → prowizja 1% kwoty

# Funkcja ma zwrócić prowizję (return).


def calculate_transfer_fee(amount):
    if amount > 1000:
        return amount / 100
    else:
        return 5


fee = calculate_transfer_fee(2500)

print(fee)
