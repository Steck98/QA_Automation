# ============================================
# ĆWICZENIE 01 — Podstawowy test funkcji
# ============================================
#
# 1. Stwórz funkcję multiply_numbers, która przyjmuje
#    dwie liczby i zwraca ich iloczyn.
#
# 2. Stwórz test dla funkcji multiply_numbers.
#
# 3. Sprawdź, czy pomnożenie liczby 3 przez 4
#    daje wynik 12.
#
# 4. Uruchom test za pomocą pytest.
#
# 5. Test powinien zakończyć się wynikiem PASS.
#
# ============================================


def multiply_numbers(a, b):
    return a * b


def test_multiply_numbers():
    assert multiply_numbers(3, 4) == 12
