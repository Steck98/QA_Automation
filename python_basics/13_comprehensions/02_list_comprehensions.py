# Masz:

# response_times = [120, 450, 80, 1200, 340, 900, 50]

# Wartości są w milisekundach.

# Utwórz za pomocą jednego list comprehension:

# slow_response_times

# które:

# bierze tylko wartości większe niż 400 ms,
# zamienia je z milisekund na sekundy (/ 1000).

response_times = [120, 450, 80, 1200, 340, 900, 50]

slow_response_times = [time / 1000 for time in response_times if time > 400]
print(slow_response_times)
