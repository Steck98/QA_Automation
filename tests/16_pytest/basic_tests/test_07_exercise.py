import pytest

# ============================================
# ĆWICZENIE 07 — Parametrize + Boundary Values
# ============================================
#
# Stwórz funkcję is_valid_age, która przyjmuje wiek.
#
# Przyjmij, że poprawny wiek znajduje się w zakresie
# od 18 do 65 lat WŁĄCZNIE.
#
# 1. Funkcja ma zwracać True dla poprawnego wieku.
#
# 2. Funkcja ma zwracać False dla niepoprawnego wieku.
#
# 3. Stwórz JEDEN test wykorzystujący parametrize.
#
# 4. Przetestuj:
#    - wartość poniżej minimum,
#    - minimum,
#    - wartość tuż powyżej minimum,
#    - wartość ze środka zakresu,
#    - wartość tuż poniżej maksimum,
#    - maksimum,
#    - wartość powyżej maksimum.
#
# 5. Wszystkie przypadki powinny znajdować się
#    w jednym @pytest.mark.parametrize().
#
# ============================================


def is_valid_age(age):
    return 18 <= age <= 65


@pytest.mark.parametrize(
    "age, expected",
    [
        (17, False),
        (18, True),
        (19, True),
        (30, True),
        (64, True),
        (65, True),
        (66, False),
    ],
)
def test_is_valid_age(age, expected):
    assert is_valid_age(age) == expected
