# Analiza sprzedaży

# Firma zbiera sprzedaż z 7 dni.

# Program ma:

# Pobrać sprzedaż z każdego dnia.
# Obliczyć:
# sumę sprzedaży,
# największą sprzedaż,
# najmniejszą sprzedaż.
# Na końcu wyświetlić:
# Weekly sales: 12450
# Highest sale: 3200
# Lowest sale: 450
# Ograniczenia
# użyj tylko tego, co już znamy,
# nie używaj list,
# nie używaj max() ani min().
max_amount = 0
min_amount = 99999999
total_sales = 0
for i in range(1, 8):
    daily_sales = int(input("How much sale you earned today ? "))
    if min_amount > daily_sales:
        min_amount = daily_sales
    if max_amount < daily_sales:
        max_amount = daily_sales
    total_sales += daily_sales
print(f"Weekly sales: {total_sales}")
print(f"Min sales: {min_amount}")
print(f"Max sales: {max_amount}")
