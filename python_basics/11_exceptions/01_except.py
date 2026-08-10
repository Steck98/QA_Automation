while True:
    try:
        product_price = float(input("Enter product price:? "))

    except ValueError:
        print("Try again, wrong value")
    else:
        if 0 < product_price:
            print(f"You ordered {product_price} products.")
            break
        else:
            print("Price cannot be negative.")
