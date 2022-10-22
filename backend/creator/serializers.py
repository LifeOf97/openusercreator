from dj_rest_auth import serializers as dj_rest_auth_serializer
from rest_framework.validators import UniqueTogetherValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.text import slugify
from .models import Openuserapp
from django.conf import settings


# Custom User model instance
AppUser = get_user_model()


class FullAppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = "__all__"


class BasicUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        exclude = (
            'id', 'is_active', 'is_staff', 'is_superuser',
            'groups', 'user_permissions', 'auth_provider_id'
         )
        extra_kwargs = {
            'password': {'write_only': True},
            'uid': {'read_only': True},
            'auth_provider': {'read_only': True},
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
        instance.gender = validated_data.get('gender', instance.gender)
        instance.is_verified = validated_data.get('is_verified', instance.is_verified)
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


class OpenuserappSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(slug_field='uid', queryset=AppUser.objects.all())

    class Meta:
        model = Openuserapp
        fields = (
            'id', 'creator', 'name', 'description', 'profiles', 'profile_password',
            'date_created', 'last_updated', 'endpoint', 'status'
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Openuserapp.objects.all(),
                fields=['creator', 'name'],
                message=_('You already have an app with that name.')
            )
        ]

    def to_internal_value(self, data):
        """
        Edited this method to provide the request user as the creator of this openuseraOpenuserapp
        instance
        """
        data['creator'] = self.context['request'].user.uid

        if data.get('name'):
            data['name'] = slugify(data['name'].replace('_', ' '))
        return super().to_internal_value(data)


# This serializers are ment for the swagger documentation
class VerifyEmailResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()


class CustomPasswordResetSerializer(dj_rest_auth_serializer.PasswordResetSerializer):

    def get_email_options(self):
        return {
            'email_template_name': 'account/email/password_reset_key_message.txt',
            'subject_template_name': 'account/email/password_reset_key_subject.txt',
            'extra_email_context': {
                'frontend_url': F'{settings.DOMAIN}/auth/help/success/reset-password',
                'wave': '\U0001F44B',
                'heart': '\U0001F499',
                'author': settings.DEVELOPER['LAST_NAME'],
                'alias': settings.DEVELOPER['ALIAS']
            }
        }
