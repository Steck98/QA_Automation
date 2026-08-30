import pytest

# ============================================
# ĆWICZENIE 09 — Projektowanie przypadków testowych
# ============================================
#
# 1. Stwórz funkcję is_valid_username, która przyjmuje
#    username jako tekst.
#
# 2. Przyjmij, że username musi mieć od 3 do 20
#    znaków, włącznie.
#
# 3. Funkcja ma zwracać True dla poprawnego username
#    oraz False dla niepoprawnego.
#
# 4. Stwórz JEDEN test wykorzystujący parametrize.
#
# 5. Samodzielnie zaprojektuj przypadki testowe.
#    Nie podaję Ci konkretnych wartości.
#
# 6. Musisz uwzględnić:
#    - przypadek poniżej minimum,
#    - minimum,
#    - wartość wewnątrz zakresu,
#    - maksimum,
#    - przypadek powyżej maksimum.
#
#
# 7. Wszystkie przypadki powinny znajdować się
#    w jednym parametrize.
#
# ============================================


def is_valid_username(username):
    return 3 <= len(username) <= 20


@pytest.mark.parametrize(
    "username, expected",
    [
        ("a" * 2, False),
        ("a" * 3, True),
        ("a" * 4, True),
        ("a" * 10, True),
        ("a" * 19, True),
        ("a" * 20, True),
        ("a" * 21, False),
    ],
)
def test_is_valid_username(username, expected):
    assert is_valid_username(username) == expected
