from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ProfileCustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'following', 'follower'), }),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(ProfileCustomUser, CustomUserAdmin)
