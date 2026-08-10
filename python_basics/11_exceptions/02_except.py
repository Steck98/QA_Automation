import json


def run_products_shop():
    with open("python_basics/11_exceptions/products.json") as file:
        products = json.load(file)
    display_products(products)
    customer_pick_product(products)


def customer_pick_product(products):
    try:
        product_choice = input("What product are you looking for? ")
        product = products[product_choice]
        product_size = get_size(product)
        print(product_size)
        product_amount = get_quantity()

    except KeyError:
        print("We don't have this product")
    else:
        print(f"Product: {product['name']}")
        print(f"Quantity: {product_amount}")
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


run_products_shop()
