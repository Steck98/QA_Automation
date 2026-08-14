from . import validators as vld


def display_products(products):
    for product in products:
        print(product)


def customer_pick_product(products):
    product_choice = input("What product are you looking for? ")
    try:
        product = products[product_choice]
    except KeyError:
        print("We don't have this product")
        return
    if product.get("sizes"):
        product_size = vld.get_size(product)
        print(product_size)
    else:
        product_size = None
        print("No available size for this product")
        product_amount = vld.get_quantity()
        product_gift = vld.get_gift_packaging()
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
