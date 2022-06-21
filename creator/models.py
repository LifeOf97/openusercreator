from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.functions import Length
from django.core import validators
from django.conf import settings
from django.db import models
from typing import List
import uuid


# Register __length
models.CharField.register_lookup(Length)


# Functiuon to create random ints
def get_random_int():
    return str(uuid.uuid4().int)[:15]


class AppUserManager(BaseUserManager):
    """
    Custom user manager.
    """
    def create_user(
        self, username: str, email: str, password: str = None, is_active: bool = True,
        is_staff: bool = False, is_superuser: bool = False
            ):
        if not username:
            raise ValueError(_("Users must provide a username"))

        if not email:
            raise ValueError(_("Users must provide email address"))

        user = self.model(username=username.lower(), email=self.normalize_email(email.lower()))
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self, username: str, email: str, password: str = None, is_active: bool = True,
        is_staff: bool = True, is_superuser: bool = True
            ):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser
        )

        user.save(using=self._db)

        return user


class AppUser(AbstractUser):
    """
    Custom user model.
    """

    id = models.BigAutoField(_("ID"), unique=True, primary_key=True, editable=False)
    uid = models.CharField(
        _("USER ID"), unique=True, editable=False,
        default=get_random_int, max_length=50, blank=False
    )

    password = models.CharField(
        _("Password"),
        max_length=128,
        validators=[
            validators.MinLengthValidator(limit_value=8),
            validators.RegexValidator(
                regex=r'\s',
                message=_("Password cannot contain spaces"),
                inverse_match=True
            )
        ]
    )

    username = models.CharField(
        _("Username"), max_length=15, unique=True, blank=False,
        validators=[
            validators.MinLengthValidator(limit_value=4),
            validators.RegexValidator(
                regex=r"\W",
                message=_("Username can only contain letters, numbers and underscore"),
                inverse_match=True
            )
        ],
        error_messages={"unique": _("This username is not available")},
    )

    first_name = models.CharField(_("First Name"), max_length=255, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=255, blank=True, null=True)
    other_name = models.CharField(_("Other Name"), max_length=255, blank=True, null=True)
    email = models.EmailField(
        _("Email Address"), unique=True, max_length=255, blank=False,
        error_messages={"unique": _("This email address belongs to another account")}
    )
    is_verified = models.BooleanField(
        _("Verified User"), default=False,
        help_text=_("Designates whether this user has verified their email address.")
    )

    objects = AppUserManager()

    USERNAME_FIELD: str = 'username'
    REQUIRED_FIELDS: List[str] = ['email']

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(username__length__gte=4), name="min_username_length"),
        ]
        ordering = ['-date_joined']

    def save(self, *args, **kwargs):
        # converts usernames to lowercase and replaces spaces with underscores
        self.username = str(self.username).replace(' ', '_').lower()
        self.email = self.email.lower()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.username

    def get_full_name(self) -> str:
        return F"{self.first_name or ''} {self.last_name or ''} {self.other_name or ''}"


class Openuser(models.Model):
    id = models.AutoField(_("ID"), primary_key=True, unique=True, editable=False)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("creator"),
        on_delete=models.CASCADE,
        help_text=_("The Appuser who owns this Openuser profiles")
    )
    name = models.CharField(
        _("Name"), max_length=20, blank=False, null=False,
        help_text=_("The name of this Openuser profile. Spaces are replaces with underscores"),
        validators=[
            validators.RegexValidator(
                regex=r'^[a-zA-Z]([\w -]*[a-zA-Z])?$',
                message=_("Must begin and end with a letter. And can only contain letters, numbers and hyphens"),
            ),
            validators.MinLengthValidator(limit_value=4)
        ]
    )
    profiles = models.IntegerField(
        _("Profiles"), blank=False, null=False, default=5,
        help_text=_("Number of openuser profiles to create, defaul is 5"),
        validators=[
            validators.MaxValueValidator(limit_value=25),
            validators.MinValueValidator(limit_value=1),
        ],
    )
    profile_password = models.CharField(
        _("Profile password"), max_length=15, blank=False,
        null=False, default='p@ssw0rd',
        help_text=_("The password to use for all profiles"),
        validators=[
            validators.RegexValidator(
                regex=r'\s',
                message=_("Profile password cannot contain spaces"),
                inverse_match=True
            )
        ]
    )
    date_created = models.DateTimeField(
        _("Date Created"), auto_now=False, auto_now_add=True,
        help_text=_("The date and time this Openuser profile was created")
    )
    last_updated = models.DateTimeField(
        _("Last Updated"), auto_now=True, auto_now_add=False,
        help_text=_("The last time this Openuser profile was updated")
    )

    class Meta:
        ordering = ['-date_created']
        constraints = [
            models.UniqueConstraint(
                fields=['creator', 'name'],
                name='unique_openuser'
            )
        ]

    def save(self, *args, **kwargs):
        self.name = str(self.name).replace(' ', '-').replace('_', '-').lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return F"{self.creator.username}-{self.name}"
