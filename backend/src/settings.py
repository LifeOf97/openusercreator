from dotenv import load_dotenv
from datetime import timedelta
from pathlib import Path
import os


# Developer detail
DEVELOPER = {
    'FIRST_NAME': 'Kelvin',
    'LAST_NAME': 'Mayowa',
    'OTHER_NAME': 'Ayeni',
    'ALIAS': 'RealestKMA',
    'CURRENT_LOCATION': 'Abuja, Nigeria'
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# load env file
if os.environ.get("ENVIRONMENT", "local") in ['production', 'docker']:
    ...
else:
    load_dotenv(dotenv_path=F"{BASE_DIR}/.env")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(' ')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my apps
    'creator.apps.CreatorConfig',
    'social_auth.apps.SocialAuthConfig',
    # third party apps
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'corsheaders',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'storages'
]


SITE_ID = 1
LANGUAGE_CODE = 'en-us'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates/"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('POSTGRES_DB', 'github_actions'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', 5432)
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

if os.environ.get('USE_AWS_S3_BUCKET', 'False') == 'True':
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = F'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    # s3 static settings
    AWS_LOCATION = 'static'
    STATIC_URL = F'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_DIRS = (os.path.join(BASE_DIR / 'staticfiles'),)
else:
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles/'


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model settings
AUTH_USER_MODEL = 'creator.AppUser'

# Authentication classes settings
AUTHENTICATION_BACKENDS = (
    'creator.authentications.AppUserBackend',
    # 'django.contrib.auth.backends.ModelBackend',
)

# Email settings
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER', 'kelvinmayoayeni@gmail.com')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_SUBJECT_PREFIX = 'Open User Creator'
EMAIL_USE_SSL = True
EMAIL_PORT = 465


# Django security Settings

CSRF_COOKIE_SAMESITE = os.environ.get("CSRF_COOKIE_SAMESITE", 'Lax')
CSRF_COOKIE_HTTPONLY = bool(os.environ.get("CSRF_COOKIE_HTTPONLY", False))
CSRF_COOKIE_SECURE = bool(os.environ.get("CSRF_COOKIE_SECURE", False))
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", 'http://localhost').split(' ')
SESSION_COOKIE_SAMESITE = os.environ.get("SESSION_COOKIE_SAMESITE", 'Lax')
SESSION_COOKIE_HTTPONLY = bool(os.environ.get("SESSION_COOKIE_HTTPONLY", False))
SESSION_COOKIE_SECURE = bool(os.environ.get("SESSION_COOKIE_SECURE", False))
SECURE_HSTS_SECONDS = int(os.environ.get("SECURE_HSTS_SECONDS", 0))
SECURE_HSTS_PRELOAD = bool(os.environ.get("SECURE_HSTS_PRELOAD", False))
SECURE_HSTS_INCLUDE_SUBDOMAINS = bool(os.environ.get("SECURE_HSTS_INCLUDE_SUBDOMAINS", False))
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

if os.environ.get('ENVIRONMENT', 'local') == 'production':
    SECURE_SSL_REDIRECT = True
else:
    SECURE_SSL_REDIRECT = False


# DjangoRestFramework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONOpenAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1'],
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


# Django rest auth settings
OLD_PASSWORD_FIELD_ENABLED = True
REST_AUTH_SERIALIZERS = {
    "PASSWORD_RESET_SERIALIZER": "creator.serializers.CustomPasswordResetSerializer"
}

# Simplejwt settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=12),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'uid',
    'USER_ID_CLAIM': 'user_uid',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=12),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


# Celery settings
if os.environ.get("ENVIRONMENT", "local") in ['production', 'docker']:
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_REDIS', 'redis://redis:6379/0')
else:
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'

CELERY_TIMEZONE = 'Africa/Lagos'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = None
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
# CELERY_BROKER_POOL_LIMIT = 1
# CELERY_BROKER_HEARTBEAT = None
# CELERY_BROKER_CONNECTION_TIMEOUT = 30
# CELERY_EVENT_QUEUE_EXPIRES = 60
# CELERY_WORKER_PREFETCH_MULTIPLIER = 1
# CELERY_WORKER_CONCURRENCY = 50


# DjSpectacular Schema settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'Openuserdata Creators API',
    'DESCRIPTION': 'The API documentation for the creators of the opeuserdata profiles.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

# Django corsheaders settings
CORS_ALLOW_CREDENTIALS = True
CORS_PREFLIGHT_MAX_AGE = 86400
CORS_ALLOWED_ORIGINS = [
    "https://openuser.xyz",
    "https://www.openuser.xyz",
    "http://127.0.0.1:8080",
]

# Domain name
DOMAIN = 'https://openuser.xyz'
