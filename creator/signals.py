from . import tasks


def new_creator(sender, instance=None, created=False, **kwargs):
    """
    Watches for the post_save signal on the custon user model so as
    to execute a celery task to email new users a verification link.
    """
    if created:
        tasks.send_email_verification.delay(instance.email)
        tasks.new_creator.delay(data={'username': instance.username, 'uid': instance.uid})


def before_delete_creator(sender, instance=None, **kwargs):
    """
    Watches for the pre_delete signal on the custom user model so as to
    execute a celery task to publish a message to rabbitmq so as to delete
    the creators openuser apps, if present on our openuserdata microservice
    listening for messages on the exchange.
    """
    try:
        creator = sender.objects.get(uid=instance.uid)
    except sender.DoesNotExist:
        pass
    else:
        for app in creator.openuser_set.all():
            tasks.delete_openuserapp(
                data={'uid': app.creator.uid, 'name': app.name}
            )


def delete_creator(sender, instance=None, **kwargs):
    """
    Watches for the post_delete signal on the openuser model so as to
    execute a celery task to publish a message to rabbitmq.
    """
    data = {'uid': instance.uid, 'username': instance.username}
    tasks.delete_creator(data=data)


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
        tasks.new_openuserapp(data=data)


def delete_openuserapp(sender, instance=None, **kwargs):
    """
    Watches for the post_delete signal on the openuser model so as to
    execute a celery task to publish a message to rabbitmq.
    """
    data = {'uid': instance.creator.uid, 'name': instance.name}
    tasks.delete_openuserapp(data=data)
