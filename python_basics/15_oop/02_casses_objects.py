# 1. Class attribute

# Klasa ma posiadać dozwolone statusy:

# 2. __init__

# Każdy test ma mieć:

# name
# duration
# status

# status ma domyślnie wynosić:

# "blocked"
# 3. Metody

# Napisz cztery metody:

# display_result()

# Wyświetla:

# Test: login_test | Status: passed | Duration: 1.2s
# change_status(new_status)

# Zmienia status tylko jeśli new_status znajduje się w allowed_statuses.

# Jeśli ktoś spróbuje:

# test.change_status("banana")

# ma wyświetlić:

# Invalid status

# i pozostawić poprzedni status.

# is_failed()

# Zwraca True albo False zależnie od statusu.

# is_slow(limit)

# Zwraca True, jeśli czas testu jest większy od podanego limit.

# 4. Utwórz 4 obiekty

# Użyj argumentów nazwanych:

# login_test
# name: login_test
# duration: 1.2
# status: passed


# payment_test
# name: payment_test
# duration: 5.8
# status: failed


# search_test
# name: search_test
# duration: 8.4
# status: passed


# registration_test
# name: registration_test
# duration: 0
# statusu NIE podawaj

# 5. Na koniec

# Wrzuć wszystkie cztery obiekty do zwykłej listy:

# dla każdego obiektu wywołaj:

# display_result()


class TestCase:
    allowed_statuses = ("passed", "failed", "skipped", "blocked")

    def __init__(self, test_name="name", duration=1.4, status="failed") -> None:

        self.test_name = test_name
        self.duration = duration
        self.status = status

    def display_result(self):
        print(
            f"Test: {self.test_name} | Status: {self.status} | Duration: {self.duration}s"
        )

    def change_status(self, new_status):
        if new_status in self.allowed_statuses:
            self.status = new_status
        else:
            print("Invalid status")

    def is_failed(self):
        return self.status == "failed"

    def is_slow(self, limit):
        return self.duration > limit


login_test = TestCase(test_name="login_test", duration=1.2, status="passed")
payment_test = TestCase(test_name="payment_test", duration=5.8, status="failed")
search_test = TestCase(test_name="search_test", duration=8.4, status="passed")
registration_test = TestCase(test_name="registration_test", duration=0)

tests = [login_test, payment_test, search_test, registration_test]

for test in tests:
    test.display_result()

failed_tests = [test for test in tests if test.is_failed()]
for test in failed_tests:
    print(test.test_name)
