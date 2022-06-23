from dj_rest_auth import serializers as dj_rest_auth_serializer
from rest_framework.validators import UniqueTogetherValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Openuser


# Custom User model instance
AppUser = get_user_model()


class FullAppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = "__all__"


class BasicAppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        exclude = ('id', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        extra_kwargs = {
            'password': {'write_only': True},
            'uid': {'read_only': True}
        }

    def to_internal_value(self, data):
        """
        Converts username and email values to lowercase.
        """
        if data.get('username'):
            data['username'] = data['username'].lower()

        if data.get('email'):
            data['email'] = data['email'].lower()

        return super().to_internal_value(data)

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = AppUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.other_name = validated_data.get('other_name', instance.other_name)
        instance.save()

        return instance


class ResendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def to_internal_value(self, data):
        if data.get('email'):
            data['email'] = data['email'].lower()

        return super().to_internal_value(data)


class LoginSerializer(serializers.Serializer):
    """
    Login serializer to facilitate the session authentication
    """
    username = serializers.CharField()
    password = serializers.CharField()


class CustomDjRestAuthLoginSerializer(dj_rest_auth_serializer.LoginSerializer):
    """"
    Custom dj_rest_auth Login_serializer class, subclassing the default LoginSerializer from dj_rest_auth
    to get rid of the email field, because the username field can server both purposes.
    """
    username = serializers.CharField()
    password = serializers.CharField()
    email = None


class CustomDjRestAuthJWTSerializer(dj_rest_auth_serializer.JWTSerializer):
    """
    Custom dj_rest_auth jwt_serializer class subclassing the default JWTSerializer to get rid of the user
    instance data returned.
    """
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    user = None


class OpenuserSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(slug_field='uid', queryset=AppUser.objects.all())

    class Meta:
        model = Openuser
        fields = (
            'id', 'creator', 'name', 'profiles', 'profile_password',
            'date_created', 'last_updated', 'endpoint'
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Openuser.objects.all(),
                fields=['creator', 'name'],
                message=_('You already have an app with that name.')
            )
        ]

    def to_internal_value(self, data):
        """
        Edited this method to provide the request user as the creator of this openuser
        instance
        """
        data['creator'] = self.context['request'].user.uid

        if data.get('name'):
            data['name'] = data['name'].replace('_', '-').replace(' ', '-').lower()
        return super().to_internal_value(data)
