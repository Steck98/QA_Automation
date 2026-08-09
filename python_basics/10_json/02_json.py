import json

with open("python_basics/10_json/orders.json") as file:
    data = json.load(file)

    for order in data:
        print(f"Order: {order['id']}")
        print(f"Customer: {order['customer']}")
        print(f"Status: {order['status']}")
        print(f"Total: {order['total']}")
        print("=============================")
    print(f"Total orders: {len(data)}")
    # -------------
    # -------------
    # -------------
    searched_order = input("What order are you looking for? ")
    order_found = False
    for order in data:
        if order["id"] == f"ORD-{searched_order}":
            print(f"Order: {order['id']}")
            print(f"Customer: {order['customer']}")
            print(f"Status: {order['status']}")
            print(f"Total: {order['total']}")
            print("=============================")
            change_status = input("Would you like to change order status? yes/no")
            if change_status == "yes":
                new_status = input("What is the new status? ")
                order["status"] = new_status
                with open("python_basics/10_json/orders.json", "w") as file:
                    json.dump(data, file, indent=4)
            order_found = True
            break
    if not order_found:
        print("Order not found.")
