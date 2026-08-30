import pytest


# ============================================
# ĆWICZENIE 03 — Niepoprawne typy danych
# ============================================
#
# 1. Zostaw funkcję multiply_numbers bez zmian.
#
# 2. Napisz test, który sprawdzi zachowanie funkcji,
#    gdy pierwszy argument jest tekstem "3".
#
# 3. Napisz test, który sprawdzi zachowanie funkcji,
#    gdy drugi argument jest tekstem "4".
#
# 4. Napisz test, który sprawdzi zachowanie funkcji,
#    gdy oba argumenty są tekstami.
#
# 5. Określ, jaki wyjątek Python zgłasza w tych przypadkach.
#
# 6. Zastosuj pytest.raises(), aby sprawdzić,
#    czy funkcja zgłasza oczekiwany wyjątek.
#
# 7. Wszystkie testy powinny przejść.
#
# ============================================
def multiply_numbers(a, b):
    return a * b


# def test_multiply_first_str_numbers():
#     assert multiply_numbers("2.5", 4) == 10


# def test_multiply_second_str_numbers():
#     assert multiply_numbers(2.5, "4") == 10


def test_multiply_two_str_numbers():
    with pytest.raises(TypeError):
        multiply_numbers("2.5", "4")
