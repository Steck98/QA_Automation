# ============================================
# ĆWICZENIE 11 — Powtarzające się dane
# ============================================
#
# 1. Stwórz funkcję get_user(), która zwraca słownik
#    zawierający:
#    - name: "Rafał"
#    - age: 28
#    - email: "raf@example.com"
#
# 2. Napisz osobny test sprawdzający imię użytkownika.
#
# 3. Napisz osobny test sprawdzający wiek użytkownika.
#
# 4. Napisz osobny test sprawdzający email użytkownika.
#
# 5. Każdy test powinien pobierać dane za pomocą
#    funkcji get_user().
#
# 6. Na razie NIE używaj fixture.
#
# 7. Zwróć uwagę, ile razy musisz pobrać/przygotować
#    te same dane.
#
# ============================================


def get_user():
    user = {"name": "Rafał", "age": 28, "email": "raf@gmail.com"}
    return user


def test_user_name():
    assert get_user()["name"] == "Rafał"


def test_user_age():
    assert get_user()["age"] == 28


def test_user_email():
    assert get_user()["email"] == "raf@gmail.com"
