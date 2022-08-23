from rest_framework_simplejwt.tokens import RefreshToken
from google_auth_oauthlib import flow as google_flow
from django.contrib.auth import get_user_model
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

User = get_user_model()
AUTH_PROVIDER = 'Google'


def google_authenticate_user(state: str, code: str):
    """
    Confirm if credentials belongs to a user in database and send refresh and
    access token to sign in user, else send data to create new account via
    google provided user info.

    state: pass the state value from the parameters passed to our google sign in
    callback url.
    code: the code value passed as a parameter to our google sign in callback url.
    """
    flow = google_flow.Flow.from_client_secrets_file(
        F'{BASE_DIR}/client_secret.json',
        scopes=[
            'https://www.googleapis.com/auth/userinfo.email',
            'https://www.googleapis.com/auth/userinfo.profile',
            'openid'
        ],
        state=state
    )

    flow.redirect_uri = "http://127.0.0.1:8000/api/v1/auth/google/get/user/"
    flow.fetch_token(code=code)

    session = flow.authorized_session()
    userinfo = session.get('https://www.googleapis.com/userinfo/v2/me').json()
    # flow.fetch_token(authorization_response=request.build_absolute_uri())
    # print(session.get('https://www.googleapis.com/auth/userinfo.email').json())
    # credentials = dict(
    #     token=flow.credentials.token,
    #     refresh_token=flow.credentials.refresh_token,
    #     token_uri=flow.credentials.token_uri,
    #     client_id=flow.credentials.client_id,
    #     client_secret=flow.credentials.client_secret,
    #     scopes=flow.credentials.scopes
    # )
    try:
        user = User.objects.get(auth_provider=AUTH_PROVIDER, auth_provider_id=userinfo['id'])
    except User.DoesNotExist:
        return dict(
            creator=False,
            username=userinfo['given_name'],
            email=userinfo['email'],
            auth_email=userinfo['email'],
            auth_provider=AUTH_PROVIDER,
            auth_provider_id=userinfo['id'],
        )
    else:
        refresh = RefreshToken.for_user(user)
        return dict(refresh=str(refresh), access=str(refresh.access_token))
