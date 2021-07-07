"""Fridges admin configuration."""

# Django
from django.contrib import admin

# Models
from .models import Fridge, Contein

@admin.register(Fridge)
class FridgeAdmin(admin.ModelAdmin):
    list_display = ('owner',)
