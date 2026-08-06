# Napisz mini system magazynowy.

# Masz listę:

# products = [
#     "Keyboard",
#     "Mouse",
#     "Monitor",
#     "Headphones",
#     "Webcam",
# ]

# Program ma:

# Wypisać wszystkie produkty z numeracją (użyj enumerate(start=1)).
# Zapytać użytkownika o numer produktu do usunięcia.
# Usunąć produkt z listy.
# Wyświetlić nową listę z numeracją.


def run_product_list():
    products = [
        "Keyboard",
        "Mouse",
        "Monitor",
        "Headphones",
        "Webcam",
    ]
    print_product_list(products)
    delete_product(products)


def print_product_list(product_list):
    for index, product in enumerate(product_list, start=1):
        print(f"Product: #{index}: {product}")


def delete_product(product_list):
    product_number = int(
        input("What is the number of the product you would like to delete? ")
    )
    product_list.pop(product_number - 1)
    print_product_list(product_list)


run_product_list()
