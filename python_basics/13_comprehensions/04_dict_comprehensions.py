# Masz:

# test_results = [
#     {"name": "login_test", "duration": 1.2},
#     {"name": "payment_test", "duration": 5.8},
#     {"name": "profile_test", "duration": 2.1},
# ]

# Za pomocą jednego dictionary comprehension utwórz:

# test_durations

test_results = [
    {"name": "login_test", "duration": 1.2},
    {"name": "payment_test", "duration": 5.8},
    {"name": "profile_test", "duration": 2.1},
]
test_durations = {
    test["name"]: test["duration"] for test in test_results if "duration" in test
}
print(test_durations)
