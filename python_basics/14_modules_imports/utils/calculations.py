def calculate_total(prices):
    return sum(prices)


def calculate_average(prices):
    return sum(prices) / len(prices)


print(f"Module name: {__name__}")

if __name__ == "__main__":
    print("I am running calculations.py directly")
