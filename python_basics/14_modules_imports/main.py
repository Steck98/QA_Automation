# import calculations as calc
# import calculations
# from calculations import calculate_average as calc_avg
import math

from utils.calculations import calculate_average, calculate_total

prices = [2, 4, 5, 6]
total = calculate_total(prices)
average = calculate_average(prices)
# average = calc_avg(prices)
# total = calc.calculate_total(prices)


print(f"Total Price: {total}")
print(f"Average: {average}")

number = 4.3
print(math.sqrt(number))
print(math.pow(number, 2))
print(math.ceil(number))
print(math.floor(number))
