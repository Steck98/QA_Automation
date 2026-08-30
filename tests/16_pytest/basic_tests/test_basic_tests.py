import pytest


def test_number():
    assert 2 + 3 == 5


def test_text_validation():
    text = "djaks"
    assert len(text) == 5


def test_input_validation():
    validation_result = True
    assert validation_result == True


# def test_negative_numbers():
#     assert get_numbers(-3, -3) == -6


# def test_positive_numbers():
#     assert get_numbers(2, 3) == 5


# def test_mixed_numbers():
#     assert get_numbers(-2, 3) == 1


def divide(number_one, number_two):
    return number_one / number_two


@pytest.mark.parametrize(
    "number_one,number_two,expected",
    [(2, 3, 5), (-2, 3, 1), (-3, -3, -6), (10, 20, 30), (0, 5, 5)],
)
def test_get_numbers(number_one, number_two, expected):
    assert number_one + number_two == expected


@pytest.mark.parametrize("n_one,n_two,res", [(10, 2, 5), (20, 5, 4), (30, 10, 3)])
def test_divide_number(n_one, n_two, res):
    assert divide(n_one, n_two) == res


def test_zer_divide():
    with pytest.raises(ZeroDivisionError) as exception:
        divide(30, 0)
    assert str(exception.value) == "division by zero"


def test_invalid_type():
    with pytest.raises(TypeError):
        divide("30", 2)
