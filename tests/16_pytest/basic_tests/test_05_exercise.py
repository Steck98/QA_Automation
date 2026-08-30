import pytest

# ============================================
# ĆWICZENIE 05 — ValueError
# ============================================
#
# 1. Stwórz funkcję convert_to_int, która przyjmuje
#    wartość i próbuje zamienić ją na liczbę całkowitą.
#
# 2. Napisz test sprawdzający poprawną konwersję:
#    tekst "123" powinien zostać zamieniony na liczbę 123.
#
# 3. Napisz test sprawdzający niepoprawną konwersję.
#    Użyj tekstu, którego nie można zamienić na liczbę
#    całkowitą.
#
# 4. Sprawdź, jaki wyjątek Python zgłasza przy takiej
#    próbie.
#
# 5. Użyj pytest.raises(), aby sprawdzić ten wyjątek.
#
# 6. Oba testy powinny przejść.
#
# ============================================


def convert_to_int(number):
    return int(number)


def test_number_conversion():
    assert convert_to_int("123") == 123


def test_invalid_number_conversion():
    with pytest.raises(ValueError):
        convert_to_int("123a")
