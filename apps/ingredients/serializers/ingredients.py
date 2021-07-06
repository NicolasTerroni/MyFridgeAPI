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

    created_by = UserModelSerializer(read_only=True)

    class Meta:
        """Meta class"""
        model = Ingredient
        fields = (
            'id',
            'name',
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
    created_by = UserModelSerializer(read_only=True)

    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
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
