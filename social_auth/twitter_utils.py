from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from urllib.parse import urlencode
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
import requests
import hashlib
import secrets
import base64
import hmac
import os


BASE_DIR = Path(__file__).resolve().parent.parent

# load env file
load_dotenv(dotenv_path=F"{BASE_DIR}/.env")

User = get_user_model()
AUTH_PROVIDER = 'Twitter'


def twitter_verify_credentials(
    method: str = 'GET',
    url: str = 'https://api.twitter.com/1.1/account/verify_credentials.json',
    oauth_token: str = None,
    oauth_token_secret: str = None,
    oauth_version: str = '1.0'
):
    """"
    Verify twitter user credentials.

    method: GET
    url: https://api.twitter.com/1.1/account/verify_credentials.json
    oauth_token: users oauth_token provided by twitter [needed]
    oauth_token_secret: users oauth_token_secret provided by twitter [needed]
    oauth_version: twitter oauth version, default is 1.0
    """
    param_url_encoded = urlencode({'': url})[1:]
    oauth_consumer_key = os.environ.get('TWITTER_API_KEY')
    oauth_consumer_secret = os.environ.get('TWITTER_API_SECRET')
    oauth_nonce = base64.b32hexencode(secrets.token_hex().encode()).decode()[:12]
    oauth_signature_method = 'HMAC-SHA1'
    oauth_timestamp = str(datetime.timestamp(datetime.now())).split('.')[0]

    param_str: str = F"include_email=true&oauth_consumer_key={oauth_consumer_key}\
        &oauth_nonce={oauth_nonce}&oauth_signature_method={oauth_signature_method}\
        &oauth_timestamp={oauth_timestamp}&oauth_token={oauth_token}\
        &oauth_version={oauth_version}&skip_status=true".replace(' ', '')

    # percent encode param str
    param_str_encoded: str = requests.utils.quote(param_str)

    # create the signature base string. should only contain 2 ampersand '&' characters
    signature_string = F"{method}&{param_url_encoded}&{param_str_encoded}"

    # percent encoded signing key
    signing_key = F"{requests.utils.quote(oauth_consumer_secret)}&{requests.utils.quote(oauth_token_secret)}"

    # calculate signature using HASH-HMAC (SHA1)
    signature = hmac.new(key=signing_key.encode(), msg=signature_string.encode(), digestmod=hashlib.sha1)
    oauth_signature = base64.b64encode(bytes.fromhex(signature.hexdigest())).decode()
    # percent encode signature
    oauth_signature_encoded = urlencode({'': oauth_signature})[1:]

    headers = F'oauth_consumer_key="{oauth_consumer_key}",oauth_nonce="{oauth_nonce}",\
        oauth_signature="{oauth_signature_encoded}",\
        oauth_signature_method="{oauth_signature_method}",\
        oauth_timestamp="{oauth_timestamp}",\
        oauth_token="{oauth_token}",oauth_version="{oauth_version}"'.replace(' ', '')

    # response = requests.get(url, headers={"Authorization": F"OAuth {OAuth}"})
    response = requests.request(
        'GET',
        url=F"{url}?include_email=true&skip_status=true",
        headers={'Authorization': F'OAuth {headers}'}
    )

    if response.status_code == 200:
        return dict(
            username=response.json()['screen_name'],
            email=response.json()['email'],
            auth_email=response.json()['email'],
            auth_token=oauth_token,
            auth_provider=AUTH_PROVIDER,
        )
    else:
        return dict(detail='Token invalid or expired. Please request a new one')


def twitter_authenticate_user(oauth_token: str, oauth_token_secret: str):
    """
    Confirm if credentials belongs to a user in database and send refresh and
    access token to sign in user, else send data to create new account via
    twitter provided details.
    """
    try:
        user = User.objects.get(auth_provider=AUTH_PROVIDER, auth_provider_token=oauth_token)
    except User.DoesNotExist:
        return twitter_verify_credentials(
            oauth_token=oauth_token,
            oauth_token_secret=oauth_token_secret
        )
    else:
        token = RefreshToken.for_user(user)
        return dict(refresh=str(token), access=str(token.access_token))
