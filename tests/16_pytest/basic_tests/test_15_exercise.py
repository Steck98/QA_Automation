import pytest

# ============================================
# ĆWICZENIE 15 — Praca ze słownikiem
# ============================================
#
# CEL:
# Przećwiczyć testowanie funkcji pracującej
# na danych zapisanych w słowniku.
#
# 1. Stwórz funkcję get_user_name(user).
#
# 2. Funkcja ma otrzymać słownik reprezentujący
#    użytkownika.
#
# 3. Słownik będzie zawierał między innymi
#    klucz "name".
#
# 4. Funkcja ma zwrócić wartość znajdującą się
#    pod kluczem "name".
#
# 5. Napisz test sprawdzający poprawne
#    pobranie imienia.
#
# 6. Przetestuj funkcję dla kilku różnych imion.
#
# 7. Wykorzystaj @pytest.mark.parametrize.
#
# 8. Napisz test sprawdzający zachowanie funkcji,
#    gdy słownik nie zawiera klucza "name".
#
# 9. Sprawdź, jaki wyjątek powinien zostać
#    w takiej sytuacji zgłoszony.
#
# ============================================


def get_user_name(user):
    return user["name"]


@pytest.mark.parametrize(
    "user_name,expect",
    [
        ({"name": "Rafał", "last_name": "Stecz"}, "Rafał"),
        ({"name": "tom", "last_name": "Riddle"}, "tom"),
        ({"name": "Angelika", "last_name": "kawasaki"}, "Angelika"),
    ],
)
def test_get_user_name(user_name, expect):
    assert get_user_name(user_name) == expect


@pytest.mark.parametrize(
    "empty_user_name",
    [
        {"last_name": "Stecz"},
        {"last_name": "Riddle"},
        {"last_name": "kawasaki"},
    ],
)
def test_get_empty_user_name(empty_user_name):
    with pytest.raises(KeyError):
        get_user_name(empty_user_name)
