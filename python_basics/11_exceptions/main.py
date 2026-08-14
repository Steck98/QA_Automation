import json

import utils.products as prd


def run_products_shop():
    try:
        with open("python_basics/11_exceptions/data/products.json") as file:
            products = json.load(file)
    except FileNotFoundError:
        print("Products file could not be found.")
    else:
        prd.display_products(products)
        prd.customer_pick_product(products)


run_products_shop()
