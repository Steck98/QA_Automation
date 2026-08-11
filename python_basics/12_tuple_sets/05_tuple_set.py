# Korzystając z tuple unpacking + set, utwórz dwa zbiory:

# yesterday_failed
# today_failed

# które mają zawierać wyłącznie nazwy testów ze statusem "failed".

# Potem za pomocą operacji na set odpowiedz na cztery pytania:

# Failed both days: ...
# Fixed today: ...
# New failures today: ...
# All tests that failed at least once: ...


yesterday_results = [
    ("login_test", "passed"),
    ("payment_test", "failed"),
    ("profile_test", "passed"),
    ("search_test", "failed"),
    ("logout_test", "passed"),
]

today_results = [
    ("login_test", "passed"),
    ("payment_test", "passed"),
    ("profile_test", "failed"),
    ("search_test", "failed"),
    ("registration_test", "passed"),
]

yesterday_failed_tests = set()
for test in yesterday_results:
    test_kind, status = test
    if status == "failed":
        yesterday_failed_tests.add(test_kind)


today_failed_tests = set()
for test in today_results:
    test_kind, status = test
    if status == "failed":
        today_failed_tests.add(test_kind)

print(yesterday_failed_tests & today_failed_tests)
print(yesterday_failed_tests | today_failed_tests)
print(yesterday_failed_tests - today_failed_tests)
print(today_failed_tests - yesterday_failed_tests)
