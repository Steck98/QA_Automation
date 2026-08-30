import pytest


# ============================================
# ĆWICZENIE 13 — Podstawowy fixture
# ============================================
#
# 1. Usuń funkcję get_user() z poprzedniego ćwiczenia.
#
# 2. Stwórz fixture o nazwie user.
#
# 3. Fixture ma przygotować słownik użytkownika:
#    - name: "Rafał"
#    - age: 28
#    - email: "raf@gmail.com"
#
# 4. Fixture ma zwracać ten słownik.
#
# 5. Zmień test sprawdzający imię tak, aby korzystał
#    z fixture user zamiast wywoływać get_user().
#
# 6. Zmień test sprawdzający wiek tak, aby korzystał
#    z fixture user.
#
# 7. Zmień test sprawdzający email tak, aby korzystał
#    z fixture user.
#
# 8. Wszystkie trzy testy powinny przejść.
#


@pytest.fixture
def user_fixture():
    return {"name": "Rafał", "age": 28, "email": "raf@gmail.com"}


def test_user_name(user_fixture):
    assert user_fixture["name"] == "Rafał"


def test_user_age(user_fixture):
    assert user_fixture["age"] == 28


def test_user_email(user_fixture):
    assert user_fixture["email"] == "raf@gmail.com"
