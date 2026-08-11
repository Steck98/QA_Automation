# Masz tuple z dozwolonymi statusami testu:

# allowed_statuses = ("passed", "failed", "skipped", "blocked")

# Napisz program, który:

# pyta użytkownika o status,
# sprawdza, czy podany status znajduje się w allowed_statuses,
# jeśli tak → Valid test status.
# jeśli nie → Invalid test status.
# następnie pętlą wyświetla wszystkie dostępne statusy.

allowed_statuses = ("passed", "failed", "skipped", "blocked")

user_status = input("What is your status? ")
if user_status in allowed_statuses:
    print("Walid test status")
else:
    print("Invalid test status")
for status in allowed_statuses:
    print(status)

print(type(("passed")))
print(type(("passed",)))
