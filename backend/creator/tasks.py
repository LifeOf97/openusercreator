from rest_framework_simplejwt.tokens import RefreshToken
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
# from django.contrib.sites.models import Site
# from rest_framework.reverse import reverse
from .pika_producers import RabbitMQProducer
from django.core.mail import send_mail
from django.conf import settings
# from .models import Openuser
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

    # domain = Site.objects.get_current().domain
    # rel_link = reverse(
    #     "creators_verify_email",
    #     kwargs={'version': settings.REST_FRAMEWORK['DEFAULT_VERSION']}
    # )
    # absolute_url = F"{domain}{rel_link}?token={token}"
    absolute_url_frontend = F"{settings.DOMAIN}/auth/verify-email?token={token}"

    body = render_to_string(
        'email_verification.txt',
        context={
            'username': user.username,
            'url': absolute_url_frontend,
            'wave': '\U0001F44B',
            'heart': '\U0001F499',
            'author': settings.DEVELOPER['LAST_NAME'],
            'alias': settings.DEVELOPER['ALIAS']
        }
    )

    send_mail(
        subject="Verify Email Address",
        message=body,
        recipient_list=[user.email, ],
        from_email=settings.DEFAULT_FROM_EMAIL
    )

    return {'Verification email sent to': user.email}


@app.task
def resend_email_verification(email):
    """
    Celery task to resend an email containing a link to verify the new user.

    email: email address of the newly created user.
    """
    user = AppUser.objects.get(email=email)
    token = RefreshToken.for_user(user).access_token

    # domain = Site.objects.get_current().domain
    # rel_link = reverse(
    #     "creators_verify_email",
    #     kwargs={'version': settings.REST_FRAMEWORK['DEFAULT_VERSION']}
    # )
    # absolute_url = F"{domain}{rel_link}?token={token}"
    absolute_url_frontend = F"{settings.DOMAIN}/auth/verify-email?token={token}"

    body = render_to_string(
        'resend_email_verification.txt',
        context={
            'username': user.username,
            'url': absolute_url_frontend,
            'wave': '\U0001F44B',
            'heart': '\U0001F499',
            'author': settings.DEVELOPER['LAST_NAME'],
            'alias': settings.DEVELOPER['ALIAS']
        }
    )

    send_mail(
        subject="Verify Email Address",
        message=body,
        recipient_list=[user.email, ],
        from_email=settings.DEFAULT_FROM_EMAIL
    )

    return {'Verification email sent to': user.email}


@app.task
def new_creator(data):
    """
    Celery task that calls a method that pushes messages to our rabbitmq message
    broker.
    """
    RabbitMQProducer().publish_message(data=data, routing_key='new_creator')
    return {'Published new creator': data['uid']}


@app.task
def delete_creator(data):
    """
    Celery task that calls a method that pushes messages to our rabbitmq message
    broker.
    """
    RabbitMQProducer().publish_message(data=data, routing_key='delete_creator')
    return {'Published delete creator': data['uid']}


@app.task
def new_openuserapp(data):
    """
    Celery task that calls a method that pushes messages to our rabbitmq message
    broker.
    """
    RabbitMQProducer().publish_message(data=data, routing_key='new_openuserapp')
    return {'Published new openuserapp': data['name']}


@app.task
def update_openuserapp(data):
    """
    Celery task that calls a method that pushes messages to our rabbitmq message
    broker.
    """
    RabbitMQProducer().publish_message(data=data, routing_key='update_openuserapp')
    return {'Published update openuserapp': data['name']}


@app.task
def delete_openuserapp(data):
    """
    Celery task that calls a method that pushes messages to our rabbitmq message
    broker.
    """
    RabbitMQProducer().publish_message(data=data, routing_key='delete_openuserapp')
    return {'Published delete openuserapp': data['name']}


# @app.task
# def activate_openuserapp(data):
#     """
#     Celery task to activate an instance of a creator's openuser app.

#     This sets the status field to Created and provides the url endpoint
#     """
#     instance = Openuser.objects.get(creator__uid=data['cid'], id=data['id'])
#     instance.status = data['status']
#     instance.endpoint = data['endpoint']
#     instance.save()
#     return {'Openuser': instance.name, "Creator": instance.creator.uid, 'status': data['status']}
