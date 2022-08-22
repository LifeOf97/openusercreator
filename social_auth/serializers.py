from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()
AUTH_PROVIDERS = (
    ('Email', 'Email'),
    ('Github', 'Github'),
    ('Google', 'Google'),
    ('Twitter', 'Twitter'),
)


class SocialUserSerializer(serializers.ModelSerializer):
    auth_email = serializers.EmailField(read_only=True)
    auth_provider = serializers.ChoiceField(choices=AUTH_PROVIDERS, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'auth_email', 'auth_provider', 'auth_provider_id')
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
        user.save()
        return user
