test_results = [
    {"name": "login_test", "status": "passed"},
    {"name": "payment_test", "status": "failed"},
    {"name": "profile_test", "status": "failed"},
    {"name": "search_test", "status": "passed"},
    {"name": "logout_test", "status": "failed"},
    {"name": "registration_test", "status": "blocked"},
]


# Jednym set comprehension utwórz:

# unique_statuses

# który da:

# {"passed", "failed", "blocked"}
test_results = {test["status"] for test in test_results}
print(test_results)
