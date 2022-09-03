from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import AppUser, Openuserapp
from django.utils.text import slugify
from django import forms


class CustomAppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = UserCreationForm.Meta.fields + ("email",)

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
        Check to make sure the creator does not have an Openuser app instance
        with the same name fields.
        """
        cleaned_data = self.cleaned_data
        name = slugify(cleaned_data.get("name").replace("_", " "))
        # creator = cleaned_data.get('creator')

        # try:
        #     app = Openuserapp.objects.get(creator=creator, id=self.initial.get('name'))
        # except Openuserapp.DoesNotExist:
        #     pass
        # else:
        #     raise forms.ValidationError(
        #         _(F"This creator already has an Openuserapp app named {name}"),
        #         code="unique_Openuser_app"
        #     )
        return name

    def clean(self):
        """
        Make sure creators cannot create more than 2 Openuser app instances.
        And if the user tries to create an app with a name that already exists
        within the creators apps, it should not be allowed.
        """
        cleaned_data = self.cleaned_data

        try:
            Openuserapp.objects.get(
                creator=cleaned_data.get("creator"), name=self.initial.get("name")
            )
        except Openuserapp.DoesNotExist:
            if Openuserapp.objects.filter(creator=cleaned_data.get("creator")).count() < 2:
                ...
            else:
                raise forms.ValidationError(
                    _("Limit reached. You already have 2 openuser apps, maximum is 2."),
                    code="limit_reached",
                )
        else:
            if (cleaned_data.get("name") != self.initial.get("name")) and \
                    Openuserapp.objects.filter(
                        creator=cleaned_data.get("creator"),
                        name=cleaned_data.get("name")
                    ).count() > 0:
                raise forms.ValidationError(
                    _(
                        F"This creator already has an Openuser app named {cleaned_data.get('name')}"
                    ),
                    code="unique_Openuser_app",
                )
            else:
                ...
                # raise forms.ValidationError(
                #     _(
                #         F"This creator already has an Openuserapp app named {cleaned_data.get('name')}"
                #     ),
                #     code="unique_Openuser_app",
                # )
        return cleaned_data
