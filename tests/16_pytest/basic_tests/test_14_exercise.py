import pytest

# ============================================
# ĆWICZENIE 14 — Testowanie pracy z listą
# ============================================
#
# CEL:
# Przećwiczyć testowanie funkcji, która
# przetwarza dane znajdujące się w liście.
#
# 1. Stwórz funkcję get_even_numbers(numbers).
#
# 2. Funkcja ma przyjmować listę liczb.
#
# 3. Funkcja ma zwracać nową listę zawierającą
#    tylko liczby parzyste.
#
# 4. Napisz podstawowy test sprawdzający,
#    czy funkcja prawidłowo wybiera liczby parzyste.
#
# 5. Przetestuj przypadek zawierający kilka
#    liczb parzystych i nieparzystych.
#
# 6. Przetestuj pustą listę.
#
# 7. Przetestuj listę zawierającą wyłącznie
#    liczby nieparzyste.
#
# 8. Przetestuj listę zawierającą wyłącznie
#    liczby parzyste.
#
# 9. Użyj @pytest.mark.parametrize tam,
#    gdzie uznasz to za sensowne.
#
# ============================================


def get_even_numbers(numbers):
    even_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def test_even_numbers():
    assert get_even_numbers([2, 4, 6]) == [2, 4, 6]


def test_empty_list():
    assert get_even_numbers([]) == []


@pytest.mark.parametrize(
    "numbers,expect", (([2, 4, 6, 8], [2, 4, 6, 8]), ([1, 3, 5, 7, 9], []), ([], []))
)
def test_mixed_numbers(numbers, expect):
    assert get_even_numbers(numbers) == expect


# @pytest.mark.parametrize("number", [2, 4, 6, 8, 12, 22, 32, 412, 122])
# def test_even_numbers(number):
#     assert get_even_numbers(number)


# @pytest.mark.parametrize("number", [1, 3, 5, 7, 9])
# def test_odd_numbers(number):
#     assert number % 2 == 1


# @pytest.mark.parametrize("number", [])
# def test_empty_numbers(number):
#     assert number % 2 == 1


# @pytest.mark.parametrize("number", [2, 4, 6, 8, 12, 22, 11, 13, 15, 91, 32, 412, 122])
# def test_mixed_numbers(number):
#     assert number % 2 == 0
