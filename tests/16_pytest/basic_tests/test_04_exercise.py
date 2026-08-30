import pytest

# ============================================
# ĆWICZENIE 04 — Testowanie konkretnego wyjątku
# ============================================
#
# 1. Stwórz funkcję divide_numbers, która przyjmuje
#    dwie liczby i zwraca wynik ich dzielenia.
#
# 2. Napisz test sprawdzający poprawne dzielenie:
#    10 / 2 powinno dać 5.
#
# 3. Napisz drugi test sprawdzający dzielenie przez 0.
#
# 4. Użyj pytest.raises(), aby sprawdzić, czy dzielenie
#    przez 0 powoduje odpowiedni wyjątek.
#
# 5. Nie zgaduj nazwy wyjątku — sprawdź, jaki wyjątek
#    rzeczywiście zgłasza Python.
#
# 6. Oba testy powinny przejść.
#
# ============================================


def divide_numbers(a, b):
    return a / b


def test_divide_numbers():
    assert divide_numbers(10, 2) == 5


def test_divide_neutral():
    assert divide_numbers(10, 1) == 10


def test_zero_number():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)
