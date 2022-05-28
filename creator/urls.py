from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from dj_rest_auth import views as dj_rest  
from . import apis


app_name = 'creator_app'


urlpatterns = [
    # auth urls
    path("auth/token/login/", dj_rest.LoginView.as_view(), name="login-via-token"),
    path("auth/token/logout/", dj_rest.LogoutView.as_view(), name="logout-via-token"),
    path("auth/session/login/", apis.LoginApiView.as_view(), name="login-via-session"),
    path("auth/session/logout/", apis.LogoutApiView.as_view(), name="logout-with-session"),
    
    
    path("creators/", apis.AppUserList.as_view({'get': 'list'}), name="creators-list"),
    path("creators/new/", apis.AppUserList.as_view({'post': 'create'}), name="creators-create"),
    path("creators/me/", apis.AppUserList.as_view({'get': 'retrieve'}), name="creators-details"),
    path("creators/me/update/", apis.AppUserList.as_view({'put': 'update', 'patch': 'update'}), name="creators-update"),
    path("creators/me/delete/", apis.AppUserList.as_view({'delete': 'destroy'}), name="creators-delete"),

]

format_suffix_patterns(urlpatterns, allowed=['json', 'xml'])