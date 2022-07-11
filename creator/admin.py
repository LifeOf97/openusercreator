from .forms import CustomAppUserCreationForm, CustomAppUserChangeForm, OpenuserModelForm
from django.contrib.auth.admin import UserAdmin
from allauth.account.admin import EmailAddress
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from .models import AppUser, Openuser
from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header: str = "Openuser Creator administration"


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
    form = OpenuserModelForm

    list_display = ('id', 'creator', 'name', 'profiles', 'status', 'date_created')
    list_display_links = ('id', 'creator', 'name')
    list_filter = ('creator', 'status')

    fieldsets = (
        ("Identification", {"fields": ("creator", "id", "name", "profile_password", "endpoint", "status")}),
        ("Data", {"fields": ("profiles", ), }),
        ("Important Dates", {"fields": ("date_created", "last_updated"), }),
    )

    readonly_fields = ('id', 'status', 'date_created', 'last_updated')
    ordering = ('-last_updated',)


admin_site = MyAdminSite(name='admin')
admin_site.register(Group)
admin_site.register(Site)
admin_site.register(EmailAddress)
admin_site.register(AppUser, AppUserAdmin)
admin_site.register(Openuser, OpenUserAdmin)
