import json


def run_orders():
    with open("python_basics/10_json/orders.json") as file:
        data = json.load(file)
    # add_order(data)
    delete_order(data)


def add_order(data):

    new_order = {
        "id": f"ORD-{input('What is the new order id? ')}",
        "customer": input("What is the new order customer name? "),
        "status": input("What is the new order status? "),
        "total": float(input("What is the new order total price? ")),
    }
    data.append(new_order)
    with open("python_basics/10_json/orders.json", "w") as file:
        json.dump(data, file, indent=4)


def delete_order(data):
    order_to_delete = input(
        "What are the last 4 digit of the id of the order that you would like to delete? "
    )
    order_found = False
    for index, order in enumerate(data):
        if order["id"] == f"ORD-{order_to_delete}":
            del data[index]
            order_found = True
            with open("python_basics/10_json/orders.json", "w") as file:
                json.dump(data, file, indent=4)
            break
    if not order_found:
        print("Order not found.")


run_orders()
