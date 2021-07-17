"""Users admin configuration."""

# Django
from django.contrib import admin

# Models
from .models import User, Profile, Fridge


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email','username','is_admin', 'is_active')

admin.site.register(User, UserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'biography')

@admin.register(Fridge)
class FridgeAdmin(admin.ModelAdmin):
    filter_horizontal = ('ingredients',)
    list_display = ('owner',)