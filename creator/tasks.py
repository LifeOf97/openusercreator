from rest_framework_simplejwt.tokens import RefreshToken
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from rest_framework.reverse import reverse
from django.core.mail import send_mail
from django.conf import settings
from src.celery import app

# Custom user model
AppUser = get_user_model()


@app.task
def send_email_verification(email):
    """
    Celery task to send an email containing a link to verify the new user.

    email: email address of the newly created user.
    """
    user = AppUser.objects.get(email=email)
    token = RefreshToken.for_user(user).access_token

    domain = Site.objects.get_current().domain
    rel_link = reverse(
        "creators_verify_email",
        kwargs={'version': settings.REST_FRAMEWORK['DEFAULT_VERSION']}
    )
    absolute_url = F"http://{domain}{rel_link}?token={token}"

    body = render_to_string(
        'email_verification.txt',
        context={
            'username': user.username,
            'url': absolute_url,
            'wave': '\U0001F44B',
            'heart': '\U0001F499',
            'author': 'Mayowa',
            'alias': 'realestKMA'
        }
    )

    send_mail(
        subject="Verify Email Address",
        message=body,
        recipient_list=[user.email, ],
        from_email=settings.DEFAULT_FROM_EMAIL
    )

    return {'emailed': user.email}


@app.task
def resend_email_verification(email):
    """
    Celery task to resend an email containing a link to verify the new user.

    email: email address of the newly created user.
    """
    user = AppUser.objects.get(email=email)
    token = RefreshToken.for_user(user).access_token

    domain = Site.objects.get_current().domain
    rel_link = reverse(
        "creators_verify_email",
        kwargs={'version': settings.REST_FRAMEWORK['DEFAULT_VERSION']}
    )
    absolute_url = F"http://{domain}{rel_link}?token={token}"

    body = render_to_string(
        'resent_email_verification.txt',
        context={
            'username': user.username,
            'url': absolute_url,
            'wave': '\U0001F44B',
            'heart': '\U0001F499',
            'author': 'Mayowa',
            'alias': 'realestKMA'
        }
    )

    send_mail(
        subject="Verify Email Address",
        message=body,
        recipient_list=[user.email, ],
        from_email=settings.DEFAULT_FROM_EMAIL
    )

    return {'emailed': user.email}
