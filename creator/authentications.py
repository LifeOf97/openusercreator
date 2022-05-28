from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


# AppUser model
AppUser = get_user_model()


class BearerAuthentication(TokenAuthentication):
    """
    Custom Token authentication to provide the Bearer name support
    """
    keyword = 'Bearer'


class AppUserBackend(ModelBackend):
    """
    Custom app user authentication backend to provide for username or email and password authentication.
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = AppUser._default_manager.get(Q(username__iexact=username) | Q(email__iexact=username))
        except AppUser.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
            return None
