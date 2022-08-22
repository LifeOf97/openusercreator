from django.urls import path
from . import apis


urlpatterns = [
    # create a new user with info provided by third party
    path(
        '<version>/auth/social/create/',
        apis.SocialUserApiView.as_view({'post': 'create'}),
        name="create_social_user"
    ),

    # social authentication url endpoints
    path(
        "<version>/auth/github/generate/url/",
        apis.GithubLoginGenerateUrl.as_view(),
        name="login_via_github"
    ),
    path(
        "<version>/auth/github/get/user/",
        apis.GithubLoginGetUser.as_view(),
        name="login_via_github_callback"
    ),
    path(
        "<version>/auth/google/generate/url/",
        apis.GoogleLoginGenerateUrl.as_view(),
        name="login_via_google"
    ),
    path(
        "<version>/auth/google/get/user/",
        apis.GoogleLoginGetUser.as_view(),
        name="login_via_google_callback"
    ),
    path(
        "<version>/auth/twitter/generate/url/",
        apis.TwitterLoginGenerateUrl.as_view(),
        name="login_via_twitter"
    ),
    path(
        "<version>/auth/twitter/get/user/",
        apis.TwitterLoginGetUser.as_view(),
        name="login_via_twitter_callback"
    ),
]
