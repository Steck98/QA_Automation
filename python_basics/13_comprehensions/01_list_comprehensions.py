# test_durations = [1.2, 5.7, 0.8, 12.4, 3.1, 8.9, 0.4]

# Za pomocą jednego list comprehension utwórz:

# slow_tests

# które będzie zawierało tylko testy trwające więcej niż 5 sekund.

test_durations = [1.2, 5.7, 0.8, 12.4, 3.1, 8.9, 0.4]
long_tests = [test for test in test_durations if test > 5]
print(long_tests)
