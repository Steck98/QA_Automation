import pytest

# ============================================
# ĆWICZENIE 06 — Parametrize
# ============================================
#
# 1. Stwórz funkcję is_even, która przyjmuje liczbę
#    i zwraca True, jeżeli liczba jest parzysta,
#    oraz False, jeżeli jest nieparzysta.
#
# 2. Przygotuj JEDEN test dla funkcji is_even.
#
# 3. Użyj @pytest.mark.parametrize(), aby uruchomić
#    ten sam test dla kilku różnych liczb.
#
# 4. Sprawdź następujące przypadki:
#    - 2 → True
#    - 4 → True
#    - 7 → False
#    - 9 → False
#    - 0 → True
#
# 5. Nie twórz pięciu osobnych funkcji testowych.
#    Ma istnieć jeden test wykorzystujący parametrize.
#
# 6. Wszystkie przypadki powinny przejść.
#
# ============================================


def is_even(number):
    return number % 2 == 0


@pytest.mark.parametrize(
    "number, expected", [(2, True), (4, True), (7, False), (9, False), (0, True)]
)
def test_is_even(number, expected):
    assert is_even(number) == expected
