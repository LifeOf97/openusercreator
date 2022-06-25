from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import AppUser, Openuser
from django.utils.text import slugify
from django import forms


class CustomAppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        return username.lower()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email.lower()


class CustomAppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = "__all__"


class OpenuserModelForm(forms.ModelForm):
    class Meta:
        model = Openuser
        fields = "__all__"

    def clean_name(self):
        """
        Check to make sure the creator does not have an openuser instance
        with the same name fields.
        """
        cleaned_data = self.cleaned_data
        name = slugify(cleaned_data.get('name').replace('_', ' '))
        creator = cleaned_data.get('creator')

        try:
            Openuser.objects.get(creator=creator, name=name)
        except Openuser.DoesNotExist:
            pass
        else:
            raise forms.ValidationError(
                _(F"This creator already has an openuser app named {name}"),
                code="unique_openuser"
            )
        return name

    def clean(self):
        """
        Make sure creators cannot create more than 2 openuser instances.
        """
        cleaned_data = self.cleaned_data

        if Openuser.objects.filter(creator=cleaned_data.get('creator')).count() < 2:
            pass
        else:
            raise forms.ValidationError(
                _("Limit reached. Creators can only have maximum of 2 openuser apps."),
                code="limit_openuser"
            )
        return cleaned_data
