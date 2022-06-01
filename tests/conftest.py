from django.contrib.auth import get_user_model
from faker import Faker
import pytest

fake = Faker()


@pytest.fixture
def app_user_model():
    return get_user_model()


@pytest.fixture
def test_user_1():
    """
    Notice that username and email fields are a mix of uppercase and lowercase letters.
    """
    return dict(
        username="TestUser1",
        email="TestUser1@gmail.com",
        password="tutu@6060f914"
    )


@pytest.fixture
def test_user_1_2():
    """
    Notice that username and email fields are a mix of uppercase and lowercase letters.
    This fixture has the same username as test_user_1 but different email.
    """
    return dict(
        username="TestUser1",
        email="TestUser2@gmail.com",
        password="tutu@6060f914"
    )


@pytest.fixture
def test_user_2():
    """
    Notice that username and email fields are a mix of uppercase and lowercase letters.
    """
    return dict(
        username="TestUser2",
        email="TestUser2@gmail.com",
        password="tutu@6060f914"
    )



@pytest.fixture
def full_user_data():
    """
    Notice that username and email fields are a mix of uppercase and lowercase letters,
    but they are converted to lowercase on save.
    """
    return dict(
        username="TestUser1",
        email="TestUser1@gmail.com",
        first_name="Test",
        last_name="User",
        other_name="Testing",
        password="tutu@6060f914"
    )


@pytest.fixture
def created(db, app_user_model, full_user_data):
    user = app_user_model.objects.create(**full_user_data)
    return user


@pytest.fixture
def created_user(db, app_user_model, test_user_1):
    user = app_user_model.objects.create_user(**test_user_1)
    return user


@pytest.fixture
def created_superuser(db, app_user_model, test_user_1):
    user = app_user_model.objects.create_superuser(**test_user_1)
    return user

