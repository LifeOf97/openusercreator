from rest_framework import views, permissions, status, viewsets, serializers
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework_simplejwt.tokens import RefreshToken
from google_auth_oauthlib import flow as google_flow
from .twitter_utils import twitter_authenticate_user
from .google_utils import google_authenticate_user
from .github_utils import github_authenticate_user
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from . import serializers as app_serializer
from urllib.parse import urlencode
from django.conf import settings
from pathlib import Path
import requests_oauthlib
import requests
import secrets
import base64
import os


# Build paths inside the project like this: HOME_DIR / 'subdir'.
HOME_DIR = Path().home()

User = get_user_model()


class SocialUserApiView(viewsets.GenericViewSet):
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = [permissions.AllowAny, ]
    serializer_class = app_serializer.SocialUserSerializer

    @extend_schema(
        responses={200: inline_serializer(
            name='Create',
            fields={'user': serializers.JSONField(), 'tokens': serializers.JSONField()}
        )}
    )
    def create(self, request, *args, **kwargs):
        """
        Create a new social user, returns the newly created users data.
        """
        serializer = self.get_serializer(data=request.data, context={'request': request})
        auth_email = serializer.initial_data['auth_email']
        auth_provider = serializer.initial_data['auth_provider']

        if serializer.is_valid():
            serializer.save(
                auth_provider=str(auth_provider).capitalize(),
                is_verified=bool(
                    serializer.validated_data['email'] == auth_email
                )
            )

            # create an authentication token to sign in the user on our system
            user = User.objects.get(
                auth_provider=str(auth_provider).capitalize(),
                auth_provider_id=serializer.validated_data['auth_provider_id']
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


class GithubLoginGenerateUrl(views.APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny, ]

    @extend_schema(
        request=None,
        responses={200: inline_serializer(name='Github', fields={'url': serializers.URLField()})}
    )
    def get(self, request, *args, **kwargs):
        authorize_url = 'https://github.com/login/oauth/authorize'

        params = urlencode(
            {
                'client_id': os.environ.get('GITHUB_CLIENT_ID'),
                'redirect_uri': F'{settings.DOMAIN}/auth/signup/social/github',
                'state': base64.b32hexencode(secrets.token_hex().encode()).decode()
            }
        )
        return Response(data={"url": F"{authorize_url}?{params}"}, status=status.HTTP_200_OK)


class GithubLoginGetUser(views.APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny, ]

    @extend_schema(
        request=None,
        responses={200: inline_serializer(
            name='Github_User',
            fields={
                'creator': serializers.BooleanField(default=False, read_only=True),
                'username': serializers.CharField(),
                'email': serializers.EmailField(),
                'auth_email': serializers.EmailField(read_only=True),
                'auth_provider': serializers.CharField(default='Github', read_only=True),
                'auth_provider_id': serializers.CharField(),
            }
        )}
    )
    def get(self, request, *args, **kwargs):
        access_url = 'https://github.com/login/oauth/access_token'

        params = urlencode(
            {
                'client_id': os.environ.get('GITHUB_CLIENT_ID'),
                'client_secret': os.environ.get('GITHUB_CLIENT_SECRET'),
                'code': dict(request.GET)['code'][0],
                'redirect_uri': F'{settings.DOMAIN}/auth/signup/social/github'
            }
        )
        headers = dict(Accept='application/json')
        response = requests.post(access_url, params=params, headers=headers)

        if response.status_code == 200:
            data = github_authenticate_user(access_token=response.json()['access_token'])
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(data={"error": "Service temporarily unavailable"}, status=status.HTTP_400_BAD_REQUEST)


class GoogleLoginGenerateUrl(views.APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny, ]

    @extend_schema(
        request=None,
        responses={200: inline_serializer(
            name='Google',
            fields={'url': serializers.URLField()}
        )}
    )
    def get(self, request, *args, **kwargs):
        flow = google_flow.Flow.from_client_secrets_file(
            F'{HOME_DIR}/.google_client_secret.json',
            scopes=[
                'https://www.googleapis.com/auth/userinfo.email',
                'https://www.googleapis.com/auth/userinfo.profile',
                'openid'
            ]
        )
        flow.redirect_uri = F'{settings.DOMAIN}/auth/signup/social/google'
        # flow.redirect_uri = "http://127.0.0.1:8000/api/v1/auth/google/get/user/"
        auth_url, state = flow.authorization_url(
            access_type='offline',
            prompt='consent',
            include_granted_scopes='true'
        )
        return Response(data={'url': auth_url}, status=status.HTTP_200_OK)


class GoogleLoginGetUser(views.APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny, ]

    @extend_schema(
        request=None,
        responses={200: inline_serializer(
            name='Google_User',
            fields={
                'creator': serializers.BooleanField(default=False, read_only=True),
                'username': serializers.CharField(),
                'email': serializers.EmailField(),
                'auth_email': serializers.EmailField(read_only=True),
                'auth_provider': serializers.CharField(default='Google', read_only=True),
                'auth_provider_id': serializers.CharField(),
            }
        )}
    )
    def get(self, request, *args, **kwargs):
        state = dict(request.GET)['state'][0]
        code = dict(request.GET)['code'][0]
        data = google_authenticate_user(state=state, code=code)
        return Response(data=data, status=status.HTTP_200_OK)


class TwitterLoginGenerateUrl(views.APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny, ]

    @extend_schema(
        request=None,
        responses={200: inline_serializer(name='Twitter', fields={'url': serializers.URLField()})}
    )
    def get(self, request, *args, **kwargs):
        """
        Returns a twitter authorize url.
        """
        request_token_url = 'https://api.twitter.com/oauth/request_token'
        authorize_token_url = 'https://api.twitter.com/oauth/authorize?oauth_token='
        # authenticate_token_url = 'https://api.twitter.com/oauth/authenticate?oauth_token='

        oauth = requests_oauthlib.OAuth1(
            client_key=os.environ.get('TWITTER_API_KEY'),
            client_secret=os.environ.get('TWITTER_API_SECRET')
        )
        data = urlencode(
            {'oauth_callback': F'{settings.DOMAIN}/auth/signup/social/twitter'}
        )

        response = requests.post(request_token_url, auth=oauth, data=data)
        auth_token = response.text.split('&')[0].split('=')[1]
        # oauth_token_secret = response.text.split('&')[1].split('=')[1]

        return Response(data={'url': F"{authorize_token_url}{auth_token}"}, status=status.HTTP_200_OK)


class TwitterLoginGetUser(views.APIView):
    """
    Twitter callkback API View
    """
    authentication_classes = []
    permission_classes = [permissions.AllowAny, ]

    @extend_schema(
        request=None,
        responses={200: inline_serializer(
            name='Twitter_User',
            fields={
                'creator': serializers.BooleanField(default=False, read_only=True),
                'username': serializers.CharField(),
                'email': serializers.EmailField(),
                'auth_email': serializers.EmailField(read_only=True),
                'auth_provider': serializers.CharField(default='Twitter', read_only=True),
                'auth_provider_id': serializers.CharField(),
            }
        )}
    )
    def get(self, request, *args, **kwargs):
        """
        Returns a twitter users data if the user is just registering for the first time
        or returns just an refresh/access token if the user is already registered in our system.
        """
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
                oauth_token_secret=data['oauth_token_secret'],
                auth_provider_id=data['user_id']
            )
            return Response(data=user, status=status.HTTP_200_OK)
        else:
            return Response(data={"error": "Service temporarily unavailable"}, status=status.HTTP_200_OK)
