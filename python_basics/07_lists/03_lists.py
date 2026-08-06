# Zadanie

# Masz:

# monthly_sales = [
#     12000,
#     18000,
#     25000,
#     32000,
#     21000,
# ]

# Nie używaj jeszcze żadnych gotowych funkcji typu sum().

# Napisz program, który wyświetli:

# Total sales:
# Average sales:
# Highest sale:
# Lowest sale:


def run_sales_counter():
    monthly_sales = [
        10,
        12000,
        18000,
        25000,
        32000,
        21000,
    ]
    print(total_sales(monthly_sales))
    print(average_sales(monthly_sales))
    print(minimum_sale(monthly_sales))
    print(maximum_sale(monthly_sales))


def total_sales(sales):
    total = 0
    for i in sales:
        total += i
    return total


def average_sales(sales):
    total = 0
    for i in sales:
        total += i
    return total / len(sales)


def minimum_sale(sales):
    min_sale = sales[0]
    for i in sales:
        if i < min_sale:
            min_sale = i
    return min_sale


def maximum_sale(sales):
    max_sale = sales[0]
    for i in sales:
        if i > max_sale:
            max_sale = i
    return max_sale


run_sales_counter()
