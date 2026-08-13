# Masz:

test_results = [
    {"name": "login_test", "status": "passed", "duration": 1.2},
    {"name": "payment_test", "status": "failed", "duration": 5.8},
    {"name": "profile_test", "status": "failed", "duration": 2.1},
    {"name": "search_test", "status": "passed", "duration": 8.4},
    {"name": "broken_test", "duration": 3.4},
]
# Zadanie

# Jednym dictionary comprehension utwórz:

# failed_test_durations

# Wynik ma być:

# {
#     "payment_test": 5.8,
#     "profile_test": 2.1
# }

failed_test_durations = {
    test["name"]: test["duration"]
    for test in test_results
    if test.get("status") == "failed"  # noqa: PLR0133
}
print(failed_test_durations)
