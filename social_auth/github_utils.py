from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
import requests


User = get_user_model()
AUTH_PROVIDER = 'Github'


def github_authenticate_user(access_token: str):
    """
    Gets the github user info using the provided access_token value, then
    confirms if credentials belongs to a user in our database and send refresh
    and access token to sign in user, else send data to create new account via
    github provided user info.

    access_token: retrieved from github access_token endpoint
    """
    user_endpoint = 'https://api.github.com/user'
    headers = dict(Authorization=F'token {access_token}')
    response = requests.get(user_endpoint, headers=headers)
    userinfo = response.json()

    try:
        user = User.objects.get(auth_provider=AUTH_PROVIDER, auth_provider_id=str(userinfo['id']))
    except User.DoesNotExist:
        return dict(
            username=userinfo['login'],
            email=userinfo['email'],
            auth_email=userinfo['email'],
            auth_provider=AUTH_PROVIDER,
            auth_provider_id=userinfo['id'],
        )
    else:
        refresh = RefreshToken.for_user(user)
        return dict(refresh=str(refresh), access=str(refresh.access_token))
