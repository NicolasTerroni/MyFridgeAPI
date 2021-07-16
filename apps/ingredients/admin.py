"""Ingredients admin configuration."""

# Django
from django.contrib import admin

# Models
from .models import Ingredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'picture', 'description', 'is_veggie', 'is_vegan')