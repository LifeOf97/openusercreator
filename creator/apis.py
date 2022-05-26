from rest_framework import status, viewsets, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from . import serializers, permissions as custom_perm


# Globall User model instance
AppUser = get_user_model()


# class AppUserList(generics.GenericAPIView):
class AppUserList(viewsets.GenericViewSet):
    queryset = AppUser.objects.all()
    serializer_class = serializers.BasicAppUserSerializer()
    lookup_field = 'username'


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
            permission_classes = [custom_perm.IsOwner]
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