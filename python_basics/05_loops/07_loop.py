# Teraz pierwszy raz wykorzystamy for do obliczeń.

# Raport sprzedaży

# Firma ma 7 dni sprzedaży.

# Nie używamy jeszcze list, więc dane pobierzemy od użytkownika.

# Program ma:

# Siedem razy zapytać:
# Enter sales for day 1:
# Enter sales for day 2:
# ...
# Enter sales for day 7:
# Zsumować wszystkie wartości.
# Na końcu wyświetlić:
# Weekly sales: 12345
# Wymagania
# użyj for,
# użyj range(),
# nie używaj while,
# nie używaj jeszcze list.

total_sales = 0
for i in range(1, 8):
    daily_sales = int(input("How much sale you earned today ? "))
    total_sales += daily_sales
print(f"Weekly sales: {total_sales}")
