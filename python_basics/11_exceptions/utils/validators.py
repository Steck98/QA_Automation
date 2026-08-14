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


def get_gift_packaging():
    while True:
        gift_package = input("Would you like it to be a gift? yes/no").lower().strip()
        print(gift_package)
        if gift_package in ["yes", "no"]:
            return gift_package
        else:
            print("Please choose yes or no.")
