from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenVerifyView
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth import views as dj_rest
from django.urls import path
from . import apis


urlpatterns = [

    # Schema urls
    # path('<version>/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('<version>/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('<version>/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('<version>/schema/', SpectacularAPIView.as_view(), name='schema'),

    # create/verify new creators urls endpoint
    path(
        "<version>/creators/new/",
        apis.AppUserApiView.as_view({'post': 'create'}),
        name="creators_create"
    ),
    path(
        "<version>/creators/new/verify-email/",
        apis.VerifyEmail.as_view(),
        name="creators_verify_email"
    ),
    path(
        "<version>/creators/new/resend-email/",
        apis.ResendVerifyEmail.as_view({'post': 'post'}),
        name="creators_resend_email"
    ),

    # creators urls endpoint
    path(
        "<version>/creators/",
        apis.AppUserApiView.as_view({'get': 'list'}),
        name="creators_list"
    ),
    path(
        "<version>/creators/me/",
        apis.AppUserApiView.as_view({'get': 'retrieve'}),
        name="creators_details"
    ),
    path(
        "<version>/creators/me/update/",
        apis.AppUserApiView.as_view({'put': 'update', 'patch': 'update'}),
        name="creators_update"
    ),
    path(
        "<version>/creators/me/delete/",
        apis.AppUserApiView.as_view({'delete': 'destroy'}),
        name="creators_delete"
    ),
    path(
        "<version>/creators/me/password/change/",
        dj_rest.PasswordChangeView.as_view(),
        name="creators_change_password"
    ),

    # openuser apps urls endpoint
    path(
        "<version>/creators/me/apps/new/",
        apis.OpenuserApiView.as_view({'post': 'create'}),
        name="creators_apps_create"
    ),
    path(
        "<version>/creators/me/apps/",
        apis.OpenuserApiView.as_view({'get': 'list'}),
        name="creators_apps_list"
    ),
    path(
        "<version>/creators/me/apps/<str:name>/",
        apis.OpenuserApiView.as_view({'get': 'retrieve'}),
        name="creators_apps_detail"
    ),
    path(
        "<version>/creators/me/apps/<str:name>/update/",
        apis.OpenuserApiView.as_view({'put': 'update', 'patch': 'update'}),
        name="creators_apps_update"
    ),
    path(
        "<version>/creators/me/apps/<str:name>/delete/",
        apis.OpenuserApiView.as_view({'delete': 'destroy'}),
        name="creators_apps_delete"
    ),

    # session authentication urls endpoint
    path(
        "<version>/auth/session/login/",
        apis.LoginSessionApiView.as_view({'post': 'post'}),
        name="login_via_session"
    ),
    path(
        "<version>/auth/session/logout/",
        apis.LogoutSessionApiView.as_view(),
        name="logout_via_session"
    ),

    # token authentication urls
    path(
        "<version>/auth/token/login/",
        dj_rest.LoginView.as_view(),
        name="login_via_token"
    ),
    path(
        "<version>/auth/token/logout/",
        dj_rest.LogoutView.as_view(),
        name="logout_via_token"
    ),
    path(
        "<version>/auth/token/verify/",
        TokenVerifyView.as_view(),
        name="token_verify"
    ),
    path(
        "<version>/auth/token/refresh/",
        get_refresh_view().as_view(),
        name="token_refresh"
    ),
]
