import pytest


def is_valid_username(username):
    return 20 >= len(username) >= 3


@pytest.mark.parametrize(
    "username, expected",
    [
        ("a" * 3, True),
        ("a" * 2, False),
        ("a" * 10, True),
        ("a" * 20, True),
        ("a" * 21, False),
    ],
)
def test_username_validation(username, expected):
    assert is_valid_username(username) == expected


def test_username_invalid_type():
    with pytest.raises(TypeError):
        is_valid_username(None)
    with pytest.raises(TypeError):
        is_valid_username(123)
