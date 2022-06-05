from .forms import CustomAppUserCreationForm, CustomAppUserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import AppUser, Openuser


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


class OpenUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'name', 'date_created', 'last_updated')
    list_display_links = ('creator', )
    list_filter = ('creator', )

    fieldsets = (
        ("Identification", {"fields": ("creator", "id", "name", "profile_password")}),
        ("Data", {"fields": ("profiles", ), }),
        ("Important Dates", {"fields": ("date_created", "last_updated"), }),
    )

    readonly_fields = ('id', 'date_created', 'last_updated')
    ordering = ('-last_updated',)


admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Openuser, OpenUserAdmin)
