"""Users admin configuration."""

# Django
from django.contrib import admin

# Models
from .models import User, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_admin', 'is_verified')

admin.site.register(User, UserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'biography')