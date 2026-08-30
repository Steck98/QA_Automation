import pytest

# ============================================
# ĆWICZENIE 13 — Klasa User
# ============================================
#
# CZĘŚĆ 1 — KLASA
#
# 1. Stwórz klasę User.
#
# 2. Dodaj __init__, który przyjmuje:
#    - name
#    - age
#    - email
#
# 3. Przechowaj wszystkie trzy wartości jako
#    prywatne atrybuty.
#
#
# CZĘŚĆ 2 — GETTERY
#
# 4. Dodaj @property dla name.
#
# 5. Dodaj @property dla age.
#
# 6. Dodaj @property dla email.
#
# 7. Sprawdź ręcznie, czy możesz odczytać:
#    user.name
#    user.age
#    user.email
#
#
# CZĘŚĆ 3 — SETTERY
#
# 8. Dodaj setter dla name.
#
# 9. Dodaj setter dla age.
#
# 10. Dodaj setter dla email.
#
# 11. Sprawdź ręcznie, czy możesz zmienić:
#     user.name
#     user.age
#     user.email
#
#
# CZĘŚĆ 4 — WALIDACJA
#
# 12. Setter age powinien pozwalać ustawić wiek
#     tylko w zakresie 18–65.
#
# 13. Jeżeli wiek jest poza zakresem, setter powinien
#     zgłosić ValueError.
#
# 14. Sprawdź ręcznie poprawną i niepoprawną wartość.
#
#
# CZĘŚĆ 5 — TESTY
#
# 15. Stwórz test sprawdzający poprawne utworzenie User.
#
# 16. Stwórz test sprawdzający odczyt name.
#
# 17. Stwórz test sprawdzający zmianę age przez setter.
#
# 18. Stwórz test sprawdzający, że niepoprawny age
#     powoduje ValueError.
#
# ============================================


class User:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if 18 <= new_age <= 65:
            self.__age = new_age
        else:
            raise ValueError("Age is out of the scope")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email


@pytest.fixture
def user_fixture():
    user = User("Rafał", 28, "raf@gmail.com")
    return user


@pytest.mark.parametrize("user_name", ["Tom", "Jan", "Rafał", "Adam"])
def test_user_name(user_fixture, user_name):
    user_fixture.name = user_name
    assert user_fixture.name == user_name


# ============================================
# ĆWICZENIE 13B — Testowanie age.setter
# ============================================
#
# 1. Wykorzystaj istniejący fixture user_fixture.
#
# 2. Napisz test ustawiający wiek na 30.
#
# 3. Sprawdź, czy user_fixture.age faktycznie
#    zmieniło się na 30.
#
# 4. Napisz osobny test sprawdzający, że ustawienie
#    wieku 17 powoduje ValueError.
#
# 5. Napisz osobny test sprawdzający, że ustawienie
#    wieku 66 powoduje ValueError.
#
# 6. Do testów nie używaj jeszcze parametrize.
#
# ============================================
@pytest.mark.parametrize("user_age", [18, 19, 64, 65])
def test_positive_user_age(user_fixture, user_age):
    user_fixture.age = user_age
    assert user_fixture.age == user_age


@pytest.mark.parametrize("user_age", [17, 66])
def test_invalid_user_age(user_fixture, user_age):
    with pytest.raises(ValueError):
        user_fixture.age = user_age
