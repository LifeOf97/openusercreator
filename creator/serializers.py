from django.utils.translation import gettext_lazy as _
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from rest_framework import serializers


# Globall User model instance
AppUser = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class FullAppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        exclude = ('password',)


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
        user = AppUser(**validated_data)

        user.set_password(validated_data['password'])
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