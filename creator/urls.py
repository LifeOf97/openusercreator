from rest_framework_simplejwt.views import TokenVerifyView
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth import views as dj_rest
from django.urls import path
from . import apis


# app_name = 'v1'


urlpatterns = [
    
    # creators retrieve, update and delete instance urls
    path("<version>/", apis.AppUserApiView.as_view({'get': 'api_schema'}, name='api_schema')),
    path("<version>/creators/", apis.AppUserApiView.as_view({'get': 'list'}), name="creators_list"),
    path("<version>/creators/me/", apis.AppUserApiView.as_view({'get': 'retrieve'}), name="creators_details"),
    path("<version>/creators/me/update/", apis.AppUserApiView.as_view({'put': 'update', 'patch': 'update'}), name="creators_update"),
    path("<version>/creators/me/delete/", apis.AppUserApiView.as_view({'delete': 'destroy'}), name="creators_delete"),
    path("<version>/creators/me/password/change/", dj_rest.PasswordChangeView.as_view(), name="creator_change_password"),
    
    # create/verify new creators account urls
    path("<version>/creators/new/", apis.AppUserApiView.as_view({'post': 'create'}), name="creators_create"),
    path("<version>/creators/new/verify-email/", apis.VerifyEmail.as_view(), name="creators_verify_email"),
    path("<version>/creators/new/resend-email/", apis.ResendVerifyEmail.as_view({'post': 'post'}), name="creators_resend_email"),
    
    # session authentication urls
    path("<version>/auth/login/session/", apis.LoginSessionApiView.as_view({'post': 'post'}), name="login_via_session"),
    path("<version>/auth/logout/session/", apis.LogoutSessionApiView.as_view({'post': 'post'}), name="logout_via_session"),

    # token authentication urls
    path("<version>/auth/login/token/", dj_rest.LoginView.as_view(), name="login_via_token"),
    path("<version>/auth/logout/token/", dj_rest.LogoutView.as_view(), name="logout_via_token"),
    path("<version>/auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("<version>/auth/token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
]
