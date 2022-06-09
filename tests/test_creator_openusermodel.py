from django.contrib.auth import get_user_model
from django.db import utils as db_exception
from creator.models import Openuser
import pytest

# Custom user model
AppUser = get_user_model()


class TestModelCase:

    @pytest.mark.django_db(transaction=True)
    def test_openuser_model_name_field_must_be_unique_per_creator(
        self,
        created,
        openuser_data
            ):
        """
        NOTE: One creator can have several Openuser profiles, however each Openuser profile
        name must be unique.
        """
        # because of the created fixture
        assert AppUser.objects.count() == 1

        # make sure that no openuser app has been create yet
        assert Openuser.objects.count() == 0

        # now create and save a new openuser profile
        app1 = Openuser.objects.create(**openuser_data)
        app1.save()

        assert Openuser.objects.count() == 1
        assert app1.creator == created

        # now create another openuser profile with the same name
        with pytest.raises(db_exception.IntegrityError) as exc_info:
            app2 = Openuser.objects.create(**openuser_data)
            app2.save()

        assert F'({created.id}, {openuser_data["name"].lower()}) already exists.' in str(exc_info.value)
        # we still have only the app1 record in our database
        assert Openuser.objects.count() == 1

    @pytest.mark.django_db(transaction=True)
    def test_openuser_model_name_field_cannot_be_more_than_20_characters(self, created):
        # because of the created fixture
        assert AppUser.objects.count() == 1

        # make sure we do not have any openuser record
        assert Openuser.objects.count() == 0

        data = dict(
            creator=created,
            name='testusernewopenuserapp',  # should not be than 20 characters.
            profiles=12,
            profile_password="password",
        )

        # now try to create and save a new openuser profile
        with pytest.raises(db_exception.DataError) as exc_info:
            app = Openuser.objects.create(**data)
            app.save()

        assert 'value too long for type character varying(20)' in str(exc_info.value)
        assert Openuser.objects.count() == 0

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.xfail
    def test_openuser_model_name_field_must_begin_with_a_letter(self, created):
        """
        NOTE: The name field in Openuser model has an RegexValidator to only allow the field to
        begin with a letter, and can only contian letters, numbers and underscores. This should
        raise a DataError, but for some reason that validator is not enforced, perhaps i need to
        use a model constraint.
        """
        # because of the created fixture
        assert AppUser.objects.count() == 1

        # make sure we do not have any openuser record
        assert Openuser.objects.count() == 0

        data = dict(
            creator=created,
            name='12app',  # cannot begin with a number.
            profiles=12,
            profile_password="password",
        )

        # now try to create and save a new openuser profile
        with pytest.raises(db_exception.DataError):
            app = Openuser.objects.create(**data)
            app.save()

        assert Openuser.objects.count() == 0

    @pytest.mark.django_db
    @pytest.mark.xfail
    def test_openuser_model_profiles_field_value_must_be_between_1_and_50(self, created):
        """
        NOTE: The profiles field in Openuser model contains a MaxValueValidator and a
        MinValueValidator to only allow the field to have values from 1 - 50 inclusive.
        This should raise a DataError, but for some reason this validators are not enforced
        when saving a model directly, perhaps i need to use a model constraint Meta field.
        """
        # because of the created fixture
        assert AppUser.objects.count() == 1

        # make sure we do not have any openuser record
        assert Openuser.objects.count() == 0

        data1 = dict(
            creator=created,
            name='MyTestApp1',
            profiles=0,  # must be greater or equal to 1
            profile_password="password",
        )

        data2 = dict(
            creator=created,
            name='MyTestApp2',
            profiles=51,  # must be less or equal to 50
            profile_password="password",
        )

        # now try to create and save a new openuser profile
        with pytest.raises(db_exception.DataError) as exc_info:
            app1 = Openuser.objects.create(**data1)
            app1.save()

        assert Openuser.objects.count() == 0
        assert 'Ensure this value is greater than or equal to 1' in str(exc_info.value)

        # now try to create and save another openuser profile
        with pytest.raises(db_exception.DataError) as exc_info:
            app2 = Openuser.objects.create(**data2)
            app2.save()

        assert Openuser.objects.count() == 0
        assert 'Ensure this value is less than or equal to 50.' in str(exc_info.value)

    @pytest.mark.django_db(transaction=True)
    def test_openuser_model_profile_password_field_cannot_be_more_than_15_characters(self, created):
        # because of the created fixture
        assert AppUser.objects.count() == 1

        # make sure we do not have any openuser record
        assert Openuser.objects.count() == 0

        data = dict(
            creator=created,
            name='MyTestApp1',
            profiles=12,
            profile_password="passwordpassword",  # not more than 15 characters
        )

        with pytest.raises(db_exception.DataError) as exc_info:
            app = Openuser.objects.create(**data)
            app.save()

        assert Openuser.objects.count() == 0
        assert 'value too long for type character varying(15)' in str(exc_info.value)

    @pytest.mark.django_db
    def test_openuser_model_uses_default_values_for_fields_not_provided_on_create(self, created):
        # because of the created fixture
        assert AppUser.objects.count() == 1

        # make sure we do not have any openuser record
        assert Openuser.objects.count() == 0

        data = dict(
            creator=created,
            name='MyTestApp1',
        )

        app = Openuser.objects.create(**data)
        app.save()

        assert Openuser.objects.count() == 1
        assert app.creator == created
        assert isinstance(app.id, int)
        assert app.profiles == 5
        assert isinstance(app.profiles, int)
        assert app.name == data['name'].lower()
        assert app.profile_password == 'p@ssw0rd'
        assert app.date_created not in ['', None]
        assert app.last_updated not in ['', None]

    @pytest.mark.django_db
    def test_openuser_model_str_method_returns_creator_username_hyphen_app_name(
        self,
        created,
        openuser_data,
        full_user_data
            ):
        """
        We need an authenticated user to create an openuser profile.
        """
        # because of the created fixture
        assert AppUser.objects.count() == 1

        # create and save a new openuser app
        app = Openuser.objects.create(**openuser_data)
        app.save()

        assert str(app) == F"{full_user_data['username'].lower()}-{openuser_data['name']}"
