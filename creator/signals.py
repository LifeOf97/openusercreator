from . import tasks


def new_creator(sender, instance=None, created=False, **kwargs):
    if created:
        tasks.send_email_verification.delay(instance.email)
