from django.urls import path
from . import apis


urlpatterns = [
    # social authentication url endpoints
    path(
        "<version>/auth/login/twitter/generate/auth/url/",
        apis.TwitterLoginGenerateAuthorizeUrl.as_view(),
        name="login_via_twitter_authorize"
    ),
    path(
        "<version>/auth/login/twitter/get/token/",
        apis.TwitterLoginGetTokens.as_view(),
        name="login_via_twitter_callback"
    )
]
