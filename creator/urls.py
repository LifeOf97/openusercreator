from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenVerifyView
from dj_rest_auth.jwt_auth import get_refresh_view
from rest_framework.schemas import get_schema_view
from dj_rest_auth import views as dj_rest
from django.urls import path
from . import apis


urlpatterns = [

    # # Schema urls
    path('<version>/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('<version>/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('<version>/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # creators retrieve, update and delete instance urls
    path('<version>/', get_schema_view(
        title="Openuser Creators APIs",
        description="API for Creators and Openuser Profiles.",
        version="1.0.0"),
        name='openapi-schema'
    ),
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
        name="creator_change_password"
    ),

    # creators openuser apps urls
    path(
        "<version>/creators/me/apps/",
        apis.OpenuserApiView.as_view({'get': 'list'}),
        name="creators_apps"
    ),
    path(
        "<version>/creators/me/apps/new/",
        apis.OpenuserApiView.as_view({'post': 'create'}),
        name="creators_apps_create"
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

    # create/verify new creators account urls
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

    # session authentication urls
    path(
        "<version>/auth/login/session/",
        apis.LoginSessionApiView.as_view({'post': 'post'}),
        name="login_via_session"
    ),
    path(
        "<version>/auth/logout/session/",
        apis.LogoutSessionApiView.as_view(),
        name="logout_via_session"
    ),

    # token authentication urls
    path(
        "<version>/auth/login/token/",
        dj_rest.LoginView.as_view(),
        name="login_via_token"
    ),
    path(
        "<version>/auth/logout/token/",
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
