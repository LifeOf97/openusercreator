from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from creator.models import Openuser
from rest_framework import status
import pytest

# Custom user model
AppUser = get_user_model()

# urls
list_my_openusers_url = reverse('creators_apps', kwargs={'version': 'v1'})
create_openuser_url = reverse('creators_apps_create', kwargs={'version': 'v1'})
# get_an_openuser_url = reverse('creators_apps_detail', kwargs={'version': 'v1'})
# update_openuser_url = reverse('creators_apps_update', kwargs={'version': 'v1'})
# delete_openuser_url = reverse('creators_apps_delete', kwargs={'version': 'v1'})
create_user_url = reverse('creators_create', kwargs={'version': 'v1'})
login_token_url = reverse('login_via_token', kwargs={'version': 'v1'})


class TestCase:

    @pytest.mark.django_db
    def test_unauthenticated_users_cannot_create_an_openuser_profile(self, openuser_data):
        client = APIClient()

        assert Openuser.objects.count() == 0

        res = client.post(create_openuser_url, openuser_data, format='json')
        assert res.status_code == status.HTTP_401_UNAUTHORIZED
        assert 'Authentication credentials were not provided' in res.data['detail']

    @pytest.mark.django_db
    def test_authenticated_users_can_create_openuser_profiles(self, created, full_user_data, openuser_data):
        client = APIClient()

        # because of the created fixture
        assert AppUser.objects.count() == 1

        # no record yet
        assert Openuser.objects.count() == 0

        # we need to login
        res = client.post(login_token_url, full_user_data, format='json')
        assert res.status_code == status.HTTP_200_OK
        assert 'access_token' in res.data
        assert 'refresh_token' in res.data

        # since we are now logged in, create a new openuser profile
        res = client.post(create_openuser_url, openuser_data, format='json')
        assert res.status_code == status.HTTP_201_CREATED
        assert Openuser.objects.count() == 1
        assert isinstance(res.data['data']['id'], int)
        assert res.data['data']['creator'] == created.username
        assert res.data['data']['name'] == openuser_data['name'].lower()
        assert res.data['data']['profiles'] == openuser_data['profiles']
        assert res.data['data']['profile_password'] == openuser_data['profile_password']
        assert res.data['data']['date_created'] not in ['', None]
        assert res.data['data']['last_updated'] not in ['', None]

    @pytest.mark.django_db
    def test_authenticated_users_cannot_create_openuser_profiles_with_same_name(
        self,
        created,
        full_user_data,
        openuser_data
            ):
        client = APIClient()

        # because of the created fixture
        assert AppUser.objects.count() == 1

        # no record yet
        assert Openuser.objects.count() == 0

        # we need to login
        res = client.post(login_token_url, full_user_data, format='json')
        assert res.status_code == status.HTTP_200_OK

        # create a new openuser profile
        res = client.post(create_openuser_url, openuser_data, format='json')
        assert res.status_code == status.HTTP_201_CREATED
        assert Openuser.objects.count() == 1

        # now try to create another openuser profile with the same name.
        res = client.post(create_openuser_url, openuser_data, format='json')
        assert res.status_code == status.HTTP_400_BAD_REQUEST
        assert 'You already have an app with that name' in str(res.data['error'])
