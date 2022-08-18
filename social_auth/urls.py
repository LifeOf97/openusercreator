from django.urls import path
from . import apis


urlpatterns = [
    # social authentication url endpoints
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
        '<version>/auth/twitter/create/',
        apis.TwitterCreateUser.as_view({'post': 'create'}),
        name="create_twitter_user"
    ),
]
