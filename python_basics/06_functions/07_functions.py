# Firma wysyła paczki.

# Koszt dostawy zależy od wagi.

# Zasady

# Do 1 kg

# 10 zł

# Powyżej 1 kg do 5 kg

# 20 zł

# Powyżej 5 kg

# 35 zł

# Jeżeli klient ma konto Premium, dostaje:

# 20% rabatu
# Program ma:

# Pobrać od użytkownika:

# wagę paczki,
# czy klient ma Premium (yes/no).

# Następnie:

# obliczyć koszt,
# wyświetlić końcową cenę.


def price_counter():
    package_weight = int(input("What is the package weight? "))
    if package_weight <= 1:
        price = 10
    elif package_weight <= 5:
        price = 20
    else:
        price = 35
    if premium_validator():
        discount = price / 100 * 20
        return price - discount
    return price


def premium_validator():
    has_premium = input("Do you have premium? yes/no").lower()
    return has_premium == "yes"


print(price_counter())
