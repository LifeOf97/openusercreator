from .forms import CustomAppUserCreationForm, CustomAppUserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import AppUser


class AppUserAdmin(UserAdmin):
    add_form = CustomAppUserCreationForm
    form = CustomAppUserChangeForm

    list_display = ('id', 'username', 'email', 'is_verified')
    list_display_links = ('id', 'username', 'email')

    add_fieldsets = (
        ("Identification", {"fields": ("username", "email")}),
        ("Security", {"fields": ("password1", "password2")}),
    )

    fieldsets = (
        ("Identification", {"fields": ("id", "uid", "username", "email", "password")}),
        ("Data", {"fields": ("first_name", "last_name", "other_name"), }),
        ("Status", {"fields": ("is_verified", "is_active", "is_staff", "is_superuser"), }),
        ("Groups & Permissions", {"fields": ("groups", "user_permissions"), }),
        ("Important Dates", {"fields": ("date_joined", "last_login"), }),
    )

    readonly_fields = ('id', 'uid', 'password', 'date_joined', 'last_login')
    ordering = ('-id',)


admin.site.register(AppUser, AppUserAdmin)
