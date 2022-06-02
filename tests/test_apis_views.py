from rest_framework.test import APIClient, RequestsClient
from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse
import pytest, pdb


AppUser = get_user_model()


@pytest.mark.django_db
def test_create_new_account_and_check_that_no_sensitive_data_is_returned_to_client(full_user_data):
    client = APIClient(enforce_csrf_checks=True)
    create_url = reverse('creators_create')

    # GET request method not allowed
    res = client.get(create_url)
    assert res.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert 'Method \"GET\" not allowed' in res.data['detail']

    # make POST request with no data
    res = client.post(create_url, format='json')
    assert res.status_code == status.HTTP_400_BAD_REQUEST

    # make POST request with data
    res = client.post(create_url, full_user_data, format='json')

    assert res.status_code == status.HTTP_201_CREATED
    assert AppUser.objects.count() == 1
    assert res.data['data']['username'] == full_user_data['username'].lower()
    assert res.data['data']['email'] == full_user_data['email'].lower()
    assert res.data['data']['first_name'] == full_user_data['first_name']
    assert res.data['data']['last_name'] == full_user_data['last_name']
    assert res.data['data']['other_name'] == full_user_data['other_name']
    assert res.data['data']['uid'] not in ['', None]
    assert not res.data['data']['is_verified']
    assert 'password' not in res.data['data']
    assert res.data['data']['date_joined']
    assert res.data['data']['last_login'] == None


@pytest.mark.django_db
def test_new_creators_can_login_via_session(full_user_data):
    client = APIClient(enforce_csrf_checks=True)
    create_url = reverse('creators_create')
    login_session_url = reverse('login_via_session')

    # GET request method not allowed
    res = client.get(login_session_url)
    assert res.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert 'Method \"GET\" not allowed' in res.data['detail']

    # make POST request with no data
    res = client.post(login_session_url, format='json')
    assert res.status_code == status.HTTP_400_BAD_REQUEST

    # register new user first
    res = client.post(create_url, full_user_data, format='json')
    assert res.status_code == status.HTTP_201_CREATED
    assert AppUser.objects.count() == 1

    # now login the new user via session login
    res = client.post(login_session_url, full_user_data, format='json')

    assert res.status_code == status.HTTP_200_OK
    assert 'Logged in successfully' in res.data['detail']
    assert res.cookies['csrftoken']
    assert res.cookies['sessionid']


@pytest.mark.django_db
def test_new_creators_can_login_via_token(full_user_data):
    client = APIClient(enforce_csrf_checks=True)
    create_url = reverse('creators_create')
    login_token_url = reverse('login_via_token')

    # GET request method not allowed
    res = client.get(login_token_url)
    assert res.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert 'Method \"GET\" not allowed' in res.data['detail']

    # make POST request with no data
    res = client.post(login_token_url)
    assert res.status_code == status.HTTP_400_BAD_REQUEST

    # register new user first
    res = client.post(create_url, full_user_data, format='json')
    assert res.status_code == status.HTTP_201_CREATED
    assert AppUser.objects.count() == 1

    # now login the new user via token login
    res = client.post(login_token_url, full_user_data, format='json')

    assert res.status_code == status.HTTP_200_OK
    assert 'access_token' in res.data
    assert 'refresh_token' in res.data
    assert res.cookies['jwt-key']
    assert res.cookies['jwt-refresh']


@pytest.mark.django_db
def test_users_who_logged_in_via_session_can_logout_via_session_providing_their_csrftoken_on_logout(created, full_user_data):
    """
    NOTE: LogoutSessionApiView requires a POST method to logout a user session, the user has to provide their
    csrftoken in the request header.
    """
    client = APIClient(enforce_csrf_checks=True)
    login_session_url = reverse('login_via_session')
    logout_session_url = reverse('logout_via_session')

    # one user in database
    assert AppUser.objects.count() == 1

    # log in user
    res = client.post(login_session_url, full_user_data, format='json')
    assert res.status_code == status.HTTP_200_OK

    # get csrftoken
    csrftoken = res.cookies['csrftoken']

    # make sure GET request method is not allowed
    res = client.get(logout_session_url)
    assert res.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert 'Method \"GET\" not allowed' in res.data['detail']

    # try to logout with passing csrftoken in request headers
    res = client.post(logout_session_url)
    assert res.status_code == status.HTTP_403_FORBIDDEN
    assert 'CSRF Failed: CSRF token missing.' in res.data['detail']
