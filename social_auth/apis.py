from rest_framework import views, permissions, status
from rest_framework.response import Response
from urllib.parse import urlencode
import requests_oauthlib
import requests
import os


class TwitterLoginGenerateAuthorizeUrl(views.APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, *args, **kwargs):
        """
        Returns a twitter authorize url.
        """
        request_token_url = 'https://api.twitter.com/oauth/request_token'
        # authorize_token_url = 'https://api.twitter.com/oauth/authorize?oauth_token='
        authenticate_token_url = 'https://api.twitter.com/oauth/authenticate?oauth_token='

        oauth = requests_oauthlib.OAuth1(
            client_key=os.environ.get('TWITTER_API_KEY'),
            client_secret=os.environ.get('TWITTER_API_SECRET')
        )
        data = urlencode(
            {'oauth_callback': 'http://127.0.0.1:8000/api/v1/auth/login/twitter/get/token/'}
        )

        response = requests.post(request_token_url, auth=oauth, data=data)
        auth_token = response.text.split('&')[0].split('=')[1]
        # oauth_token_secret = response.text.split('&')[1].split('=')[1]

        return Response(data={'url': F"{authenticate_token_url}{auth_token}"}, status=status.HTTP_200_OK)


class TwitterLoginGetTokens(views.APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, *args, **kwargs):
        access_token_url = "https://api.twitter.com/oauth/access_token"
        oauth = requests_oauthlib.OAuth1(
            client_key=os.environ.get('TWITTER_API_KEY'),
            client_secret=os.environ.get('TWITTER_API_SECRET')
        )

        params = dict(request.GET)
        data = urlencode({
            'oauth_verifier': params['oauth_verifier'][0],
            'oauth_token': params['oauth_token'][0]
        })

        response = requests.post(access_token_url, auth=oauth, data=data)
        data = {d.split('=')[0]: d.split('=')[1] for d in response.text.split('&')}
        return Response(data=data, status=status.HTTP_200_OK)
