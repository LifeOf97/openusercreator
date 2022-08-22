from django.urls import path
from . import apis


urlpatterns = [
    # social authentication url endpoints
    path(
        "<version>/auth/google/generate/url/",
        apis.GoogleLoginObtainAccessToken.as_view(),
        name="login_via_google_authorize"
    ),
    path(
        "<version>/auth/google/get/user/",
        apis.GoogleLoginGetUser.as_view(),
        name="login_via_google_callback"
    ),
    path(
        "<version>/auth/twitter/generate/url/",
        apis.TwitterLoginGenerateUrl.as_view(),
        name="login_via_twitter_authorize"
    ),
    path(
        "<version>/auth/twitter/get/user/",
        apis.TwitterLoginGetUser.as_view(),
        name="login_via_twitter_callback"
    ),
    path(
        '<version>/auth/social/create/',
        apis.SocialUserApiView.as_view({'post': 'create'}),
        name="create_social_user"
    ),
]
