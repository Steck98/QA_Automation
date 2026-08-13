# test_results = [
#     {"name": "login_test", "status": "passed", "duration": 1.2},
#     {"name": "payment_test", "status": "failed", "duration": 5.8},
#     {"name": "profile_test", "status": "failed", "duration": 2.1},
#     {"name": "search_test", "status": "passed", "duration": 8.4},
#     {"name": "logout_test", "status": "failed", "duration": 0.9},
# ]

# Zadanie: jednym list comprehension utwórz:

# failed_tests

# które będzie zawierało tylko nazwy testów ze statusem "failed".

test_results = [
    {"name": "login_test", "status": "passed", "duration": 1.2},
    {"name": "payment_test", "status": "failed", "duration": 5.8},
    {"name": "profile_test", "status": "failed", "duration": 2.1},
    {"name": "search_test", "status": "passed", "duration": 8.4},
    {"name": "logout_test", "status": "failed", "duration": 0.9},
]

failed_tests = [test["name"] for test in test_results if test["status"] == "failed"]
print(failed_tests)

# Utwórz jednym list comprehension:

# slow_failed_tests

# które zawiera nazwy tylko tych testów, które jednocześnie:

# mają "status": "failed"
# trwały dłużej niż 1 sekundę

# Oczekiwany wynik:
slow_failed_tests = [
    test["name"]
    for test in test_results
    if test["status"] == "failed" and test["duration"] > 1
]
print(slow_failed_tests)
