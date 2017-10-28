from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Profile
from .forms import UserAdminCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):
    form = UserAdminForm
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'email')
        }),
        ('Basic Info', {
            'fields': ('last_login', )
        }),
        (
            'Permissions', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
                )
            }
        )
    )
    list_display = ['username', 'email', 'is_active', 'is_staff', 'created']


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
