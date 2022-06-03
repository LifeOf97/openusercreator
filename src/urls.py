from django.views.generic import RedirectView
from django.conf.urls.static import static
from dj_rest_auth import views as dj_rest
from django.urls import path, include
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='api/creators/')),  # redirect to the api urls.
    path('api/', include('creator.urls')),  # api urls

    # reset password via email urls
    path("api/auth/help/password/reset/", dj_rest.PasswordResetView.as_view(), name="password_reset"),
    path(
        "api/auth/help/password/reset/confirm/<str:uidb64>/<str:token>/",
        dj_rest.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),

]

if settings.DEBUG:
    urlpatterns + [
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ]
