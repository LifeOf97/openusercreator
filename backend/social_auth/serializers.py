from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
AUTH_PROVIDERS = (
    ('Email', 'Email'),
    ('Github', 'Github'),
    ('Google', 'Google'),
    ('Twitter', 'Twitter'),
)


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Example one',
            summary='Sign in with (Github, Google or Twitter)',
            description="Create a new user, using the user info returned by the social platform.",
            value={
                'username': 'string',
                'email': 'example@email.com',
                'auth_email': 'example@email.com',
                'auth_provider': 'string',
                'auth_provider_id': 'string',
                'password': 'string',
            },
            request_only=True,
            response_only=False
        )
    ]
)
class SocialUserSerializer(serializers.ModelSerializer):
    auth_email = serializers.EmailField(read_only=True)
    auth_provider = serializers.ChoiceField(choices=AUTH_PROVIDERS, read_only=True)

    class Meta:
        model = User
        fields = (
            'uid', 'email', 'username', 'password', 'auth_email', 'auth_provider',
            'auth_provider_id', 'date_joined', 'last_login', 'is_verified'
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

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
