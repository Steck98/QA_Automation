# Mini projekt — Kasa sklepu

# Masz napisać program, który pyta użytkownika o:

# Nazwę produktu
# Cenę jednej sztuki
# Ilość sztuk
# Kwotę pieniędzy, którą klient daje kasjerowi


product_name = input("What product would you like to buy?")
product_price = float(input("What is the price of it ?"))
product_amount = int(input("How many would you like to buy?"))
total_to_pay = product_price * product_amount
print(f"Product: {product_name}")
print(f"Price per item: {product_price}")
print(f"Quantity: {product_amount}")
print(f"Total: {total_to_pay}")
user_payed = float(input("How much money you gave"))
print(f"Paid: {user_payed}")
user_change = user_payed - total_to_pay
print(f"Change: {user_change}")
