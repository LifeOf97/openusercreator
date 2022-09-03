from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import AppUser, Openuserapp
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


class OpenUserAppModelForm(forms.ModelForm):
    class Meta:
        model = Openuserapp
        fields = "__all__"

    def clean_name(self):
        """
        Check to make sure the creator does not have an Openuserapp instance
        with the same name fields.
        """
        cleaned_data = self.cleaned_data
        name = slugify(cleaned_data.get('name').replace('_', ' '))
        creator = cleaned_data.get('creator')

        try:
            Openuserapp.objects.get(creator=creator, name=name)
        except Openuserapp.DoesNotExist:
            pass
        else:
            raise forms.ValidationError(
                _(F"This creator already has an Openuserapp app named {name}"),
                code="unique_Openuserapp"
            )
        return name

    def clean(self):
        """
        Make sure creators cannot create more than 2 Openuserapp instances.
        """
        cleaned_data = self.cleaned_data

        if Openuserapp.objects.filter(creator=cleaned_data.get('creator')).count() < 2:
            pass
        else:
            raise forms.ValidationError(
                _("Limit reached. Creators can only have a maximum of 2 Openuserapp."),
                code="limit_Openuserapp"
            )
        return cleaned_data
