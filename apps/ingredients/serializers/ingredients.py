"""Ingredients serializers."""

# Models
from apps.ingredients.models import Ingredient

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Serializers
from apps.users.serializers import UserModelSerializer


class IngredientModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""

    created_by = serializers.StringRelatedField()

    class Meta:
        """Meta class"""
        model = Ingredient
        fields = (
            'id',
            'name',
            'slug_name',
            'created_by',
            'picture',
            'description',
            'is_veggie',
            'is_vegan'
        )


class CreateIngredientSerializer(serializers.ModelSerializer):
    """Handle the ingredient creation."""

    name = serializers.CharField(
        validators= [UniqueValidator(
            queryset = Ingredient.objects.all(),
            message = "This ingredient was already created.")],
    )
    slug_name = serializers.CharField(
        validators= [UniqueValidator(
            queryset = Ingredient.objects.all(),
            message = "This slug name was already used.")],
    )
    created_by = serializers.StringRelatedField() # make Stringrelated

    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'slug_name',
            'created_by',
            'picture',
            'description',
            'is_veggie',
            'is_vegan'
            )

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        return super().create(validated_data)
