# Firma wypłaca premie pracownikom.

# Program pobiera:

# miesięczną sprzedaż,
# liczbę spóźnień,
# liczbę lat pracy.
# Zasady
# Premia sprzedażowa

# Jeżeli sprzedaż wynosi:

# poniżej 20 000 → 0 zł
# od 20 000 → 500 zł
# od 50 000 → 1500 zł

# Kara za spóźnienia

# Jeżeli pracownik miał:

# 0 spóźnień → 0 zł kary
# 1–3 → 100 zł
# powyżej 3 → 300 zł
# Premia za staż

# Jeżeli pracuje:

# minimum 5 lat → 500 zł
# minimum 10 lat → 1000 zł
# Wynik

# Program ma wypisać:

# Sales bonus: ...
# Experience bonus: ...
# Penalty: ...
# -------------------
# Final bonus: ...


def run_bonus_calculator():
    monthly_sales = int(input("How many sales you achieved this month? "))
    delays_amount = int(input("How many times you had delays at work? "))
    working_years = int(input("How many years are you working with us? "))

    sales_bonus = sale_bonus(monthly_sales)
    years_bonus = experience_bonus(working_years)
    delay_penalty = penalty(delays_amount)

    final_bonus = sales_bonus + years_bonus - delay_penalty

    print(f"Sales bonus: {sales_bonus}")
    print(f"Experience bonus: {years_bonus}")
    print(f"Penalty: {delay_penalty}")
    print("-------------------")
    print(f"Final bonus: {final_bonus}")


def sale_bonus(sales):
    if sales >= 50000:
        return 1500
    if sales >= 20000:
        return 500
    else:
        return 0


def experience_bonus(experience):
    if experience >= 10:
        return 1000
    if experience >= 5:
        return 500
    else:
        return 0


def penalty(delays):
    if 1 <= delays <= 3:
        return 100
    if delays > 3:
        return 300
    else:
        return 0


run_bonus_calculator()
