# Dostajesz:

# yesterday_errors = {
#     "LoginError",
#     "TimeoutError",
#     "DatabaseError",
#     "PaymentError",
# }

# today_errors = {
#     "LoginError",
#     "DatabaseError",
#     "ValidationError",
#     "APIError",
# }

# Wyświetl:

# Errors on both days: ...
# All errors: ...
# Fixed errors: ...
# New errors: ...

# Gdzie sam musisz ustalić, której operacji użyć, żeby:

# both days = wystąpiły wczoraj i dzisiaj,
# all = wszystkie unikalne z obu dni,
# fixed = były wczoraj, ale dzisiaj już ich nie ma,
# new = dzisiaj są, ale wczoraj ich nie było.

yesterday_errors = {
    "LoginError",
    "TimeoutError",
    "DatabaseError",
    "PaymentError",
}

today_errors = {
    "LoginError",
    "DatabaseError",
    "ValidationError",
    "APIError",
}
print(yesterday_errors & today_errors)

print(yesterday_errors | today_errors)

print(yesterday_errors - today_errors)

print(today_errors - yesterday_errors)
print(yesterday_errors ^ today_errors)
