from rest_framework import views, permissions, status, viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from .twitter_utils import twitter_authenticate_user
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from urllib.parse import urlencode
from . import serializers
import requests_oauthlib
import requests
import os

User = get_user_model()
AUTH_PROVIDER = 'Twitter'


class TwitterLoginGenerateUrl(views.APIView):
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
            {'oauth_callback': 'http://127.0.0.1:8000/api/v1/auth/twitter/get/user/'}
        )

        response = requests.post(request_token_url, auth=oauth, data=data)
        auth_token = response.text.split('&')[0].split('=')[1]
        # oauth_token_secret = response.text.split('&')[1].split('=')[1]

        return Response(data={'url': F"{authenticate_token_url}{auth_token}"}, status=status.HTTP_200_OK)


class TwitterLoginGetUser(views.APIView):
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

        if response.status_code == 200:
            data = {d.split('=')[0]: d.split('=')[1] for d in response.text.split('&')}
            user = twitter_authenticate_user(
                oauth_token=data['oauth_token'],
                oauth_token_secret=data['oauth_token_secret']
            )
            return Response(data=user, status=status.HTTP_200_OK)
        else:
            return Response(data={"error": "Service temporarily unavailable"}, status=status.HTTP_200_OK)


class TwitterCreateUser(viewsets.GenericViewSet):
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = [permissions.AllowAny, ]
    serializer_class = serializers.TwitterRegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        auth_email = serializer.initial_data['auth_email']

        if serializer.is_valid():
            serializer.save(
                is_verified=bool(
                    serializer.validated_data['email'] == auth_email
                )
            )

            # create an authentication token to sign in the user on our system
            user = User.objects.get(
                auth_provider=AUTH_PROVIDER,
                auth_provider_token=serializer.data['auth_provider_token']
            )
            # create new authentication refresh/access tokens
            refresh = RefreshToken.for_user(user)
            # pass the created auth tokens to the response data
            return Response(
                data={
                    "user": serializer.data,
                    "tokens": {"refresh": str(refresh), "access": str(refresh.access_token)}
                },
                status=status.HTTP_201_CREATED
            )
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
