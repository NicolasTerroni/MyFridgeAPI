"""Fridges admin configuration."""

# Django
from django.contrib import admin

# Models
from .models import Fridge

@admin.register(Fridge)
class FridgeAdmin(admin.ModelAdmin):
    filter_horizontal = ('ingredients',)
    list_display = ('owner',)
