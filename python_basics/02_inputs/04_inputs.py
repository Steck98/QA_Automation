# Tworzysz prosty kalkulator zakupów.

# Program pyta użytkownika o:

# cenę produktu,
# ilość sztuk.

# Następnie wyświetla:
# Total price: 59.97

product_price = float(input("What is the price of the product that you want to buy?"))
product_amount = int(input("What is the amount of products that you want to buy?"))
total_price = product_amount * product_price

print(f"Total price: {total_price}")
