from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status, views, viewsets, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from . import serializers, permissions as custom_perm
from dj_rest_auth.jwt_auth import unset_jwt_cookies
from drf_spectacular.types import OpenApiTypes
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.conf import settings
from .models import Openuserapp
from . import tasks
import jwt

# Custom user model instance
User = get_user_model()


class UserApiView(viewsets.GenericViewSet):
    """
    User Generic API Viewset.
    """
    queryset = User.objects.all()
    serializer_class = serializers.BasicUserSerializer

    def get_object(self, *args, **kwargs):
        """
        Edited so as to return the object instance of the currently logged in user.
        """
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, username=self.request.user.username)

        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self, *args, **kwargs):
        if (self.action == 'create') or \
                str(reverse('creators_create', kwargs={'version': 'v1'})).endswith(self.request.path):
            permission_classes = [permissions.AllowAny]
        elif self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [custom_perm.IsOwner & permissions.IsAuthenticated]
        return [perm() for perm in permission_classes]

    def list(self, request, *args, **kwargs):
        """
        Returns a list of all creators in the system.
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Creates a new creator account.
        Returns data of the creator.
        """
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()

            # create an authentication token to sign in the user on our system
            user = User.objects.get(
                auth_provider='Email',
                uid=serializer.data['uid']
            )
            # create new authentication refresh/access tokens
            refresh = RefreshToken.for_user(user)
            return Response(
                data={
                    "user": serializer.data,
                    "tokens": {"refresh": str(refresh), "access": str(refresh.access_token)}
                },
                status=status.HTTP_201_CREATED
            )
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns data of the currently logged in creator.
        """
        serializer = self.get_serializer(self.get_object(), context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """
        Updates the data of the currently logged in creator.
        Returns the newly updated instance.
        """
        serializer = self.get_serializer(
            instance=self.get_object(),
            data=request.data,
            context={'request': request},
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Deletes the currently logged in creator from the system permanently.
        Returns deleted creator's data
        """
        user = self.get_object()
        username, email, uid = user.username, user.email, user.uid
        data = {'username': username, 'email': email, 'uid': uid, 'detail': 'Deleted successfully'}
        user.delete()
        response = Response(data=data, status=status.HTTP_204_NO_CONTENT)

        # clears jwt authentication if present
        unset_jwt_cookies(response)
        return response


class ResendVerifyEmail(viewsets.GenericViewSet):
    serializer_class = serializers.ResendEmailSerializer

    def post(self, request, *args, **kwargs):
        """
        Resends a new verificaton email.
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            # check if email belongs to the currently logged in user.
            if request.user.email == serializer.data['email']:
                tasks.resend_email_verification.delay(serializer.data['email'])
                return Response(data={"detail": _(F"A verification link has been sent to {serializer.data['email']}")})

            return Response(
                data={"error": _(F"Email address {serializer.data['email']} is not associated to your account")},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(views.APIView):
    permission_classes = []

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='token',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Token'
            )
        ],
        responses={200: serializers.VerifyEmailResponseSerializer}
    )
    def get(self, request, *args, **kwargs):
        """
        Gets the token from the url address and verifies a users account email address.
        Returns success or Failure.
        """
        token = request.GET.get('token')

        try:
            check_token = jwt.decode(token, key=settings.SECRET_KEY, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            return Response(
                data={"error": _('Activation link expired, please request a new one.')},
                status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.DecodeError:
            return Response(
                data={"error": _('Invalid token, please request a new one.')},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            user = User.objects.get(uid=check_token['user_uid'])

            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response(data={"detail": _("Email address verified successfully")}, status=status.HTTP_200_OK)

            return Response(
                data={"detail": _("Your email address has already been verified")},
                status=status.HTTP_208_ALREADY_REPORTED
            )


class OpenuserappApiView(viewsets.GenericViewSet):
    lookup_field = 'name'
    queryset = Openuserapp.objects.all()
    serializer_class = serializers.OpenuserappSerializer

    def get_queryset(self):
        creator = self.request.user
        return creator.openuserapp_set.all()

    def list(self, request, *args, **kwargs):
        """
        Returns a list of Openuserapp apps that belongs to the currently
        authenticated creator.
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, name=None, *args, **kwargs):
        """
        Returns the data of the requested openuseraOpenuserapp instance of the currently
        authenticated creator.
        """
        serializer = self.get_serializer(self.get_object(), context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Creates a new openuseraOpenuserapp instance for the currently authenticated creator.
        Returns the newly created openuseraOpenuserapp data.
        """
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if self.get_queryset().count() < 2:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data={'error': _('Limit reached. You can only have a maximum of 2 openuser apps.')},
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, *args, **kwargs):
        """
        Updates a particular openuseraOpenuserapp data for the currently authenticated creator.
        Returns the updated openuseraOpenuserapp data.
        """
        serializer = self.get_serializer(
            instance=self.get_object(),
            data=request.data,
            context={'request': request},
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Deletes an openuseraOpenuserapp instance of the currently authenticated creator.
        Returns a limited data of the deleted instance data.
        """
        openuseraOpenuserapp = self.get_object()
        name, profiles = openuseraOpenuserapp.name, openuseraOpenuserapp.profiles
        openuseraOpenuserapp.delete()
        return Response(
            data={'name': name, 'profiles': profiles, 'detail': _('Deleted successfully')},
            status=status.HTTP_204_NO_CONTENT
        )


# class LoginSessionApiView(viewsets.GenericViewSet):
#     authentication_classes = []
#     permission_classes = [permissions.AllowAny]
#     serializer_class = serializers.LoginSerializer

#     def post(self, request, *args, **kwargs):
#         """
#         Accepts the following post parameters: username/email, password, to
#         login a creator via session.
#         """
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             user = authenticate(
#                 request,
#                 username=serializer.validated_data['username'],
#                 password=serializer.validated_data['password']
#             )

#             if user is not None:
#                 login(request, user)
#                 response = Response(data={"detail": _("Logged in successfully")}, status=status.HTTP_200_OK)

#                 # clear jwt (access & refresh) tokens if present
#                 unset_jwt_cookies(response)

#                 return response  # return logged in response to client

#             return Response(data={"detail": _("wrong username/password")}, status=status.HTTP_400_BAD_REQUEST)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LogoutSessionApiView(views.APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     authentication_classes = [authentication.SessionAuthentication]

#     def post(self, request, *args, **kwargs):
#         """
#         Logs out a session authenticated user.
#         """
#         logout(request)
#         return Response(data={"detail": _("Logged out successfully")}, status=status.HTTP_200_OK)
