from . import tasks


def new_creator(sender, instance=None, created=False, **kwargs):
    """
    Watches for the post_save signal so as to execute a celery
    task to email new users a verification link.
    """
    if created:
        tasks.send_email_verification.delay(instance.email)
