from . import tasks


def new_creator(sender, instance=None, created=False, **kwargs):
    """
    Watches for the post_save signal so as to execute a celery
    task to email new users a verification link.
    """
    if created:
        tasks.send_email_verification.delay(instance.email)
        tasks.publish_new_creator.delay(data={'username': instance.username, 'uid': instance.uid})
