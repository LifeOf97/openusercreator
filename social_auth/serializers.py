from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()
AUTH_PROVIDER = 'Twitter'
AUTH_PROVIDERS = (
    ('Email', 'Email'),
    ('Github', 'Github'),
    ('Google', 'Google'),
    ('Twitter', 'Twitter'),
)


class TwitterRegisterUserSerializer(serializers.ModelSerializer):
    auth_email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'auth_email', 'auth_provider_token')
        extra_kwargs = {
            'password': {'write_only': True},
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
        # we do not need the auth_email field in database
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.auth_provider = AUTH_PROVIDER
        user.save()
        return user
