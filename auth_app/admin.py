"""Auth app models admin."""

# Django
from django.contrib import admin

# Models
from auth_app.models import (
    AuthAppShopUser
)


@admin.register(AuthAppShopUser)
class AuthAppShopUserAdmin(admin.ModelAdmin):
    """AuthAppShopUser model admin."""

    list_display = ('myshopify_domain', 'token', 'password', 'last_login')