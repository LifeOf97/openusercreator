from django.contrib.auth import get_user_model
from django.db import utils as db_exception
import pytest

# Custom user model
AppUser = get_user_model()


class TestClass:

    @pytest.mark.django_db
    def test_appusermodel_create_user_method_only_sets_users_as_active(self, created_user):
        assert created_user.is_active
        assert not created_user.is_staff
        assert not created_user.is_superuser


    @pytest.mark.django_db
    def test_appusermodel_create_superuser_method_sets_users_as_active_staff_and_superuser(self, created_superuser):
        assert created_superuser.is_active
        assert created_superuser.is_staff
        assert created_superuser.is_superuser


    @pytest.mark.django_db
    def test_appusermodel_new_users_are_not_verified(self, created_user):
        assert not created_user.is_verified


    @pytest.mark.django_db
    def test_appusermodel_username_and_email_are_converted_to_lowercase(self, created):
        assert str(created.email).islower()
        assert str(created.username).islower()


    @pytest.mark.django_db
    def test_appusermodel_str_method_returns_users_username(self, created):
        assert str(created) == created.username


    @pytest.mark.django_db
    def test_appusermodel_username_field_is_unique_cannot_save_username_if_already_exists(self, test_user_1, test_user_1_2):
        user_1 = AppUser.objects.create_user(**test_user_1)

        with pytest.raises(db_exception.IntegrityError) as exc_info:
            user_2 = AppUser.objects.create_user(**test_user_1_2)

        assert exc_info.type is db_exception.IntegrityError
        assert F"Key (username)=({test_user_1['username'].lower()}) already exists" in str(exc_info.value)


    @pytest.mark.django_db
    def test_appusermodel_username_is_lowercased_and_replaces_spaces_with_undescores(self):
        user_data = dict(
            username="Test User",
            email="TestUser@gmail.com",
            password="tutu@6060f914"
        )
        user = AppUser.objects.create_user(**user_data)

        assert user.username == user_data['username'].replace(' ', '_').lower()


    @pytest.mark.django_db
    @pytest.mark.xfail
    def test_appusermodel_username_can_only_contain_letters_numbers_and_underscores(self):
        """
        This test is expected to fail. the AppUser Model username field uses a Regex
        validator to allow only letters, numbers and underscores, but for some reasons
        this model test passes with a wrong username input. [Debug in process]...
        """
        user_data = dict(
            username="Test@User",
            email="TestUser@gmail.com",
            password="tutu@6060f914"
        )

        with pytest.raises(db_exception.DataError) as exc_info:
            user = AppUser.objects.create_user(**user_data)

        assert AppUser.objects.count() == 1


    @pytest.mark.django_db
    def test_appusermodel_username_field_cannot_be_greater_than_15_characters(self):
        user_data = dict(
            username="testusernamecannotbemorethan15characters",
            email="TestUser@gmail.com",
            password="tutu@6060f914"
        )

        with pytest.raises(db_exception.DataError) as exc_info:
            user = AppUser.objects.create_user(**user_data)

        assert exc_info.type == db_exception.DataError 
        assert "value too long for type character varying(15)" in str(exc_info.value)


    @pytest.mark.django_db
    def test_appusermodel_username_cannot_be_less_than_4_characters(self):
        user_data = dict(
            username="tes",
            email="TestUser@gmail.com",
            password="tutu@6060f914"
        )

        with pytest.raises(db_exception.IntegrityError) as exc_info:
            user = AppUser.objects.create_user(**user_data)

        assert exc_info.type == db_exception.IntegrityError 
        assert 'violates check constraint "min_username_length"' in str(exc_info.value)

    
    @pytest.mark.django_db
    def test_appusermodel_email_field_is_unique_cannot_save_email_if_already_exists(self, test_user_1_2, test_user_2):
        user_1 = AppUser.objects.create_user(**test_user_1_2)

        with pytest.raises(db_exception.IntegrityError) as exc_info:
            user_2 = AppUser.objects.create_user(**test_user_2)

        assert exc_info.type is db_exception.IntegrityError
        assert F"Key (email)=({test_user_1_2['email'].lower()}) already exists" in str(exc_info.value)


    @pytest.mark.django_db
    @pytest.mark.xfail
    def test_appusermodel_password_field_cannot_be_less_than_8_characters(self):
        """
        This test is expected to fail but does not. the AppUser Model password field uses
        MinLengthValidator to only accept password greater than or equal to 8, but for some
        reasons this model test passes with a wrong password input. [Debug in process]...
        """
        user_data = dict(
            username="testuser",
            email="TestUser@gmail.com",
            password="tutu"
        )

        with pytest.raises(db_exception.DataError) as exc_info:
            user = AppUser.objects.create_user(**user_data)

        assert AppUser.objects.count() == 1