import pytest


@pytest.fixture
def number():
    return 10


def test_number(number):
    assert number == 10


@pytest.fixture
def username():
    return "Rafał"


def test_username(username):
    assert username == "Rafał"


@pytest.fixture
def user():
    return {"name": "Rafał", "age": 28, "email": "Raf@gmail.com"}


def test_user_name(user):
    assert user["name"] == "Rafał"


def test_user_age(user):
    assert user["age"] == 28


def test_user_higher_age(user):
    assert user["age"] >= 18


def test_user_mail(user):
    assert user["email"] == "Raf@gmail.com"


@pytest.fixture
def user_data():
    print("SETUP")

    data = {"value": 10}

    yield data

    print("TEARDOWN")


def test_value(user_data):
    assert user_data["value"] == 10
