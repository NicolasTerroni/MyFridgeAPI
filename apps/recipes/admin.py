"""Recipes admin configuration."""

# Django
from django.contrib import admin

# Models
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture', 'instructions', 'is_veggie', 'is_vegan')