# Dostajesz listę wyników testów:

# test_errors = [
#     "TimeoutError",
#     "LoginError",
#     "TimeoutError",
#     "DatabaseError",
#     "LoginError",
#     "TimeoutError",
#     "ValidationError",
# ]

# Bez tworzenia ręcznie nowego zbioru:

# Zamień test_errors na set.
# Wyświetl wszystkie unikalne typy błędów.

# Wyświetl:

# Unique errors: 4

# Sprawdź za pomocą in, czy wystąpił "DatabaseError" i jeśli tak:

# Database error detected.

test_errors = [
    "TimeoutError",
    "LoginError",
    "TimeoutError",
    "DatabaseError",
    "LoginError",
    "TimeoutError",
    "ValidationError",
]

unique_errors = set(test_errors)
print(unique_errors)
print(f"Unique errors: {len(unique_errors)}")
if "DatabaseError" in unique_errors:
    print("Database error detected.")
