# ============================================
# ĆWICZENIE 02 — Testowanie różnych przypadków
# ============================================
#
# 1. Zostaw funkcję multiply_numbers bez zmian.
# 2. Dodaj test mnożenia dwóch liczb ujemnych.
# 3. Dodaj test mnożenia liczby przez 0.
# 4. Dodaj test mnożenia liczby dziesiętnej przez liczbę całkowitą.
# 5. Uruchom wszystkie testy w tym pliku.
# 6. Wszystkie testy powinny przejść.
#
# ============================================
def multiply_numbers(a, b):
    return a * b


def test_multiply_negative_numbers():
    assert multiply_numbers(-3, -4) == 12


def test_multiply_neutral_numbers():
    assert multiply_numbers(10, 0) == 0


def test_multiply_float_numbers():
    assert multiply_numbers(2.5, 4) == 10
