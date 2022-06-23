from . import tasks


def new_creator(sender, instance=None, created=False, **kwargs):
    """
    Watches for the post_save signal on the custon user model so as
    to execute a celery task to email new users a verification link.
    """
    if created:
        tasks.send_email_verification.delay(instance.email)
        tasks.publish_new_creator.delay(data={'username': instance.username, 'uid': instance.uid})


def new_openuserapp(sender, instance=None, created=False, **kwargs):
    """
    Watches for the post_save signal on the openuser model so as to
    execute a celery task to publish a message to rabbitmq.
    """
    if created:
        data = {
            'uid': instance.creator.uid,
            'name': instance.name,
            'profiles': instance.profiles,
            'profile_password': instance.profile_password,
        }
        tasks.publish_create_openuserapp(data=data)
