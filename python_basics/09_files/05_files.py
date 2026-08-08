# with open("python_basics/09_files/orders.txt", "w") as file:
#     print()


def run_order_list():
    orders = load_orders()
    display_order(orders)
    search_order_status(orders)
    user_update_order = input("Would you like to update an order ? yes/no")
    if user_update_order == "yes":
        update_order(orders)
        orders = load_orders()
    user_new_order = input("Would you like to place a new order ? yes/no")
    if user_new_order == "yes":
        new_order()
        orders = load_orders()
    user_delete_order = input("Would you like to delete an order ? yes/no")
    if user_delete_order == "yes":
        delete_order(orders)
        orders = load_orders()
    display_order(orders)


def display_order(orders):
    for line in orders:
        print(line)


def search_order_status(orders):
    user_search_result = input(
        "What are the 4 last order numbers you are looking for? "
    )
    if f"ORD-{user_search_result}" in orders:
        print("Order Found.")
    else:
        print("Order Not Found.")


def load_orders():
    with open("python_basics/09_files/orders.txt") as file:
        content = []
        for line in file:
            content.append(line.strip())
        return content


def new_order():
    with open("python_basics/09_files/orders.txt", "a") as file:
        new_user_order = input("What is the new order 4 digit number? ")
        file.write(f"ORD-{new_user_order}\n")


def delete_order(orders):
    delete_user_order = input(
        "What are the 4 last digits of the order that would you like to delete? "
    )
    orders.remove(f"ORD-{delete_user_order}")
    with open("python_basics/09_files/orders.txt", "w") as file:
        for order in orders:
            file.write(f"{order}\n")


def update_order(orders):
    user_select_order = input("What order would you like to update? ")
    for index, order in enumerate(orders):
        if order == f"ORD-{user_select_order}":
            new_user_order = input("What is the new order? ")
            print(index, order)
            orders[index] = f"ORD-{new_user_order}"
    with open("python_basics/09_files/orders.txt", "w") as file:
        for order in orders:
            file.write(f"{order}\n")


run_order_list()
