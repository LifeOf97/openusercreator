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
        openuser_data_1
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
        app1 = Openuser.objects.create(**openuser_data_1)
        app1.save()

        assert Openuser.objects.count() == 1
        assert app1.creator == created

        # now create another openuser profile with the same name
        with pytest.raises(db_exception.IntegrityError) as exc_info:
            app2 = Openuser.objects.create(**openuser_data_1)
            app2.save()

        assert F'Key (creator_id, name)=({created.id}, newapi1) already exists.' in str(exc_info.value)
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
            name='testusernewopenuserapp',  # more than 20 charaters.
            profiles=12,
            profile_password="password",
        )

        # now try to create and save a new openuser profile
        with pytest.raises(db_exception.DataError) as exc_info:
            app = Openuser.objects.create(**data)
            app.save()

        assert 'value too long for type character varying(20)' in str(exc_info.value)
        assert Openuser.objects.count() == 0

    @pytest.mark.django_db
    def test_openuser_model_str_method_returns_creator_username_and_app_name(
        self,
        created,
        openuser_data_1,
        full_user_data
            ):
        """
        We need an authenticated user to create an openuser profile.
        """
        # because of the created fixture
        assert AppUser.objects.count() == 1

        # create and save a new openuser app
        app = Openuser.objects.create(**openuser_data_1)
        app.save()

        assert str(app) == F"{full_user_data['username'].lower()} {openuser_data_1['name']}"
