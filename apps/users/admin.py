from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_admin', 'is_verified')


admin.site.register(User, UserAdmin)