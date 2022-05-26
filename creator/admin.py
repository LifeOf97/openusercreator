from django.contrib import admin
from .models import AppUser


class AppUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'username', 'email')
    list_display_links = ('id', 'uid', 'username')

    fieldsets = (
        ("Identification", {"fields": ("id", "uid", "username", "email", "password")}),
        ("Data", {"fields": ("first_name", "last_name", "other_name"),}),
        ("Status", {"fields": ("is_verified", "is_active", "is_staff", "is_superuser"),}),
        ("Groups & Permissions", {"fields": ("groups", "user_permissions"),}),
        ("Important Dates", {"fields": ("date_joined", "last_login"),}),
    )
    
    readonly_fields = ('id', 'uid', 'password', 'date_joined', 'last_login')
    ordering = ('-id',)


admin.site.register(AppUser, AppUserAdmin)