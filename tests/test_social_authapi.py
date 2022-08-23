from rest_framework.reverse import reverse
from rest_framework.test import APIClient
import pytest
import os


@pytest.mark.parametrize(
    "endpoint, value",
    [
        (
            reverse('login_via_github', kwargs={'version': 'v1'}),
            F"https://github.com/login/oauth/authorize?client_id={os.environ.get('GITHUB_CLIENT_ID')}&redirect_uri="
        ),
        (
            reverse('login_via_google', kwargs={'version': 'v1'}),
            F"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=\
{os.environ.get('GOOGLE_CLIENT_ID')}&redirect_uri="
        ),
        (
            reverse('login_via_twitter', kwargs={'version': 'v1'}),
            "https://api.twitter.com/oauth/authenticate?oauth_token="
        )
    ]
)
def test_a_get_request_to_login_via_social_account_returns_a_valid_url(endpoint, value):
    client = APIClient()
    response = client.get(endpoint, format='json')

    assert response.status_code == 200
    assert str(response.data['url']).startswith(value)
