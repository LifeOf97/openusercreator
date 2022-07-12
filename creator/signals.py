# Please note: all signals in this module are explicitly registered in the apps.py file
from . import tasks


def new_creator(sender, instance=None, created=False, **kwargs):
    """
    Watches for the post_save signal on the custom user model so as
    to execute a celery task to email new users a verification link and
    also another task to publish message to our message broker.
    """
    if created:
        tasks.send_email_verification.delay(instance.email)
        tasks.new_creator.delay(data={'username': instance.username, 'uid': instance.uid})


def delete_creator(sender, instance=None, **kwargs):
    """
    Watches for the post_delete signal on the custom user model so
    as to execute a celery task to publish a message to our message
    broker.
    """
    tasks.delete_creator.delay(data={'uid': instance.uid, 'username': instance.username})


def new_openuserapp(sender, instance=None, created=False, **kwargs):
    """
    Watches for the post_save signal on the openuser model so as to
    execute a celery task to publish a message to rabbitmq.
    """
    data = {
        'uid': instance.creator.uid,
        'id': instance.id,
        'name': instance.name,
        'profiles': instance.profiles,
        'profile_password': instance.profile_password,
    }

    if created:  # if newly created
        tasks.new_openuserapp.delay(data=data)
    else:
        tasks.update_openuserapp.delay(data=data)


def delete_openuserapp(sender, instance=None, **kwargs):
    """
    Watches for the post_delete signal on the openuser model so as to
    execute a celery task to publish a message to rabbitmq.
    """
    tasks.delete_openuserapp.delay(
        data={
            'uid': instance.creator.uid,
            'id': instance.id,
            'name': instance.name
        }
    )
