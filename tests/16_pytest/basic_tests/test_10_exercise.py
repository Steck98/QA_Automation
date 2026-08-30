import pytest

# ============================================
# ĆWICZENIE 10 — Puste wartości
# ============================================
#
# 1. Stwórz funkcję is_valid_text, która przyjmuje
#    tekst jako argument.
#
# 2. Funkcja ma zwracać False, jeżeli otrzyma pusty
#    string.
#
# 3. Funkcja ma zwracać True, jeżeli otrzyma tekst
#    zawierający przynajmniej jeden znak.
#
# 4. Stwórz jeden test wykorzystujący parametrize.
#
# 5. Przetestuj co najmniej:
#    - pusty string,
#    - jeden znak,
#    - normalny tekst.
#
# 6. Wszystkie przypadki umieść w jednym parametrize.
#
# ============================================


def is_valid_text(text):
    return len(text) >= 1


@pytest.mark.parametrize("text, expected", [("", False), ("a", True), (" ", True)])
def test_is_valid_text(text, expected):
    assert is_valid_text(text) == expected
