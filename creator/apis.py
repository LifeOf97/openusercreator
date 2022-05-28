from rest_framework import status, views, viewsets, permissions
from django.contrib.auth import authenticate, login, logout
from . import serializers, permissions as custom_perm
from django.contrib.auth import get_user_model
from rest_framework.response import Response


# Globall User model instance
AppUser = get_user_model()


class LoginApiView(views.APIView):
    """
    Login view with username and password usign django's built in authenticate and login functions.
    """
    authentication_classes = []
    permission_classes = [permissions.AllowAny,]
    serializer_class = serializers.LoginSerializer


    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])

            if user is not None:
                login(request, user)
                return Response(data={"detail": "Logged in successfully"}, status=status.HTTP_200_OK)

            return Response(data={"detail": "wrong username/password"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LogoutApiView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        logout(request)
        return Response(data={"detail": "Logged out successfully"})


class AppUserList(viewsets.GenericViewSet):
    lookup_field = 'username'
    queryset = AppUser.objects.all()
    serializer_class = serializers.BasicAppUserSerializer()


    def get_serializer_class(self):
        if self.request.user.is_staff:
            return serializers.FullAppUserSerializer
        return serializers.BasicAppUserSerializer


    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [custom_perm.IsOwnerOrStaff]
        return [perm() for perm in permission_classes]


    def list(self, request, format=None):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def create(self, request, format=None):
        serializer = serializers.BasicAppUserSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, username, format=None):
        serializer = self.get_serializer(self.get_object(), context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    
    def update(self, request, username, format=None):
        serializer = serializers.BasicAppUserSerializer(instance=self.get_object(), data=request.data, context={'request': request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def destroy(self, request, username, format=None):
        appuser = self.get_object()
        username, uid = appuser.username, appuser.uid
        appuser.delete()
        return Response(data={'username': username, 'uid': uid, 'detail': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)