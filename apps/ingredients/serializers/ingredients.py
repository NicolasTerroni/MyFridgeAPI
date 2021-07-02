"""Ingredients serializers."""

# Models
from apps.ingredients.models import Ingredient

# Django REST Framework
from rest_framework import serializers


class IngredientModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""

    class Meta:
        """Meta class"""
        model = Ingredient
        fields = (
            'id',
            'name',
            'picture',
            'description',
            'is_veggie',
            'is_vegan'
        )