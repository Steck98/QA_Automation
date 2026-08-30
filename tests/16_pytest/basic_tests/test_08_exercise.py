import pytest

# ============================================
# ĆWICZENIE 08 — Walidacja długości tekstu
# ============================================
#
# 1. Stwórz funkcję is_valid_password, która przyjmuje
#    hasło jako tekst.
#
# 2. Przyjmij, że poprawne hasło musi mieć od 8 do 20
#    znaków, włącznie.
#
# 3. Funkcja ma zwracać True dla poprawnego hasła
#    oraz False dla niepoprawnego.
#
# 4. Stwórz JEDEN test wykorzystujący parametrize.
#
# 5. Przetestuj:
#    - hasło krótsze niż minimum,
#    - hasło dokładnie na minimum,
#    - hasło trochę powyżej minimum,
#    - hasło ze środka zakresu,
#    - hasło trochę poniżej maksimum,
#    - hasło dokładnie na maksimum,
#    - hasło dłuższe niż maksimum.
#
# 6. Wykorzystaj generowanie tekstu za pomocą mnożenia
#    stringa przez liczbę, zamiast ręcznie wpisywać
#    bardzo długie hasła.
#
# 7. Wszystkie przypadki powinny znajdować się
#    w jednym parametrize.
#
# ============================================


def is_valid_password(password):
    return 8 <= len(password) <= 20


@pytest.mark.parametrize(
    "password, expected",
    [
        ("a" * 7, False),
        ("a" * 8, True),
        ("a" * 9, True),
        ("a" * 14, True),
        ("a" * 19, True),
        ("a" * 20, True),
        ("a" * 21, False),
    ],
)
def test_is_valid_password(password, expected):
    assert is_valid_password(password) == expected
