from django.contrib.auth import get_user_model
from faker import Faker
import pytest

fake = Faker()


@pytest.fixture
def AppUser():
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
        username="FullUser1",
        email="FullUser1@gmail.com",
        first_name="Full",
        last_name="User",
        other_name="Fulling",
        password="fufu@6060f914"
    )


@pytest.fixture
def another_user_data():
    """
    Notice that username and email fields are a mix of uppercase and lowercase letters,
    but they are converted to lowercase on save.
    """
    return dict(
        username="AnotherUser1",
        email="AnotherUser1@gmail.com",
        first_name="Another",
        last_name="User",
        other_name="Anothering",
        password="tutu@6060f914"
    )


@pytest.fixture
def created(db, AppUser, full_user_data):
    user = AppUser.objects.create(**full_user_data)
    user.set_password(full_user_data['password'])
    user.save()

    return user


@pytest.fixture
def created_user(db, AppUser, test_user_1):
    user = AppUser.objects.create_user(**test_user_1)
    return user


@pytest.fixture
def created_superuser(db, AppUser, test_user_1):
    user = AppUser.objects.create_superuser(**test_user_1)
    return user
