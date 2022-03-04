"""Django Admin Core app model."""
from django.contrib import admin   # noqa:F401
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    """Custom admin user model."""

    ordering = ['id']
    list_display = ['email', 'firstname', 'lastname', 'telephone']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('firstname', 'lastname', 'telephone')}),
        
    )

    add_fieldsets = ((None, {
                     'classes': ('wide',),
                     'fields': ('email', 'password1', 'password2'), }), )

admin.site.register(models.User, UserAdmin)
