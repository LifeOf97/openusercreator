from django.contrib.auth import get_user_model
from django.db.models.signals import (
    pre_save, post_save, pre_delete, post_delete,
    m2m_changed
)
from creator.models import Openuser
import pytest


@pytest.fixture(autouse=True)
def disable_signals(request):
    """
    Fixture to disable django signals before tests then restore it after.
    Credit: https://www.cameronmaske.com/muting-django-signals-with-a-pytest-fixture/
    """
    if 'enable_signals' in request.keywords:
        # do not apply this fixture if marked with 'enable_signals'
        return

    signals = [
        pre_save,
        post_save,
        pre_delete,
        post_delete,
        m2m_changed
    ]
    restore = {}

    for signal in signals:
        # keep signal receivers so as to restore later
        restore[signal] = signal.receivers
        # detach signal receivers
        signal.receivers = []

    def restore_signals():
        # Restore signal method
        for signal, receivers in restore.items():
            signal.receiver = receivers

    request.addfinalizer(restore_signals)


@pytest.fixture
def User():
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
def created(db, User, full_user_data):
    user = User.objects.create(**full_user_data)
    user.set_password(full_user_data['password'])
    user.save()

    return user


@pytest.fixture
def created_user(db, User, test_user_1):
    """
    This fixture creates a new user using the data from test_user_1
    """
    user = User.objects.create_user(**test_user_1)
    return user


@pytest.fixture
def created_superuser(db, User, test_user_1):
    """
    This fixture creates a new superuser using the data from test_user_1
    """
    user = User.objects.create_superuser(**test_user_1)
    return user


@pytest.fixture
def openuser_data(created):
    """
    This fixture provides data to create an openuser app, it uses the created fixture
    as the creator of this instance.
    """
    return dict(
        creator=created,
        name='new-1-app',
        profiles=12,
        profile_password="password",
    )


@pytest.fixture
def openuser_data_1():
    """
    This fixture provides data to create an openuser app, it uses the created fixture
    as the creator of this instance.
    """
    return dict(
        name='New-1-App',
        profiles=12,
        profile_password="mypassword",
    )


@pytest.fixture
def created_openuser_1(created):
    """
    This fixture provides data to create an openuser app, it uses the created fixture
    as the creator of this instance.
    """
    data = dict(
        creator=created,
        name='New-1-App',
        profiles=12,
        profile_password="mypassword",
    )
    app = Openuser.objects.create(**data)
    app.save()
    return app


@pytest.fixture
def created_openuser_2(created):
    """
    This fixture provides data to create an openuser app, it uses the created fixture
    as the creator of this instance.
    """
    data = dict(
        creator=created,
        name='New-2-App',
        profiles=12,
        profile_password="mypassword",
    )
    app = Openuser.objects.create(**data)
    app.save()
    return app


@pytest.fixture
def created_openuser_3(created):
    """
    This fixture provides data to create an openuser app, it uses the created fixture
    as the creator of this instance.
    """
    data = dict(
        creator=created,
        name='New-3-App',
        profiles=12,
        profile_password="mypassword",
    )
    app = Openuser.objects.create(**data)
    app.save()
    return app


@pytest.fixture
def created_openuser_4(created_user):
    """
    This fixture provides data to create an openuser app, it uses the created_user fixture
    as the creator of this instance.
    """
    data = dict(
        creator=created_user,
        name='New-1-App',
        profiles=12,
        profile_password="mypassword",
    )
    app = Openuser.objects.create(**data)
    app.save()
    return app


@pytest.fixture
def created_openuser_5(created_user):
    """
    This fixture provides data to create an openuser app, it uses the created_user fixture
    as the creator of this instance.
    """
    data = dict(
        creator=created_user,
        name='New-2-App',
        profiles=12,
        profile_password="mypassword",
    )
    app = Openuser.objects.create(**data)
    app.save()
    return app


@pytest.fixture
def created_openuser_6(created_user):
    """
    This fixture provides data to create an openuser app, it uses the created_user fixture
    as the creator of this instance.
    """
    data = dict(
        creator=created_user,
        name='New-3-App',
        profiles=12,
        profile_password="mypassword",
    )
    app = Openuser.objects.create(**data)
    app.save()
    return app
