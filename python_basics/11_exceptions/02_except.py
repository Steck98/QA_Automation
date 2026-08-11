import json


def run_products_shop():
    try:
        with open("python_basics/11_exceptions/products.json") as file:
            products = json.load(file)
    except FileNotFoundError:
        print("Products file could not be found.")
    else:
        display_products(products)
        customer_pick_product(products)


def customer_pick_product(products):
    product_choice = input("What product are you looking for? ")
    try:
        product = products[product_choice]
    except KeyError:
        print("We don't have this product")
    if product.get("sizes"):
        product_size = get_size(product)
        print(product_size)
    else:
        product_size = None
        print("No available size for this product")
        product_amount = get_quantity()
        product_gift = get_gift_packaging()
        print(f"Product: {product['name']}")
        print(f"Quantity: {product_amount}")
        if product_gift == "yes":
            print("Gift packaging: Yes")
        try:
            print(f"Total: {product['price'] * product_amount}")
        except TypeError:
            print("Product price is invalid. Please contact support.")
        finally:
            print("--- End of purchase attempt ---")


def get_size(product):
    if product["sizes"]:
        print("Available sizes:")
        for index, size in enumerate(product["sizes"], start=1):
            print(f"{index}. {size}")
        while True:
            try:
                pick_size = int(input("Choose size:"))
                if pick_size > len(product["sizes"]) or pick_size < 1:
                    raise IndexError
            except IndexError:
                print("Selected size does not exist")
            except ValueError:
                print("Size choice must be a number.")
            else:
                picked_size = product["sizes"][pick_size - 1]
                return picked_size


def get_quantity():

    while True:
        try:
            product_amount = int(input("How many would you like to buy"))
            if product_amount <= 0:
                raise ValueError
        except ValueError:
            print("Quantity must be a whole number greater than 0.")
        else:
            return product_amount


def display_products(products):
    for product in products:
        print(product)


def get_gift_packaging():
    while True:
        gift_package = input("Would you like it to be a gift? yes/no").lower().strip()
        print(gift_package)
        if gift_package in ["yes", "no"]:
            return gift_package
        else:
            print("Please choose yes or no.")


run_products_shop()
