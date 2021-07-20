"""Recipes serializers."""

# Models
from apps.ingredients.models import ingredients
from apps.recipes.models import Recipe

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RecipeModelSerializer(serializers.ModelSerializer):
    """Recipes model serializer."""

    created_by = serializers.StringRelatedField()

    class Meta:
        """Meta class"""
        model = Recipe
        fields = (
            'id',
            'name',
            'slug_name',
            'created_by',
            'picture',
            'description',
            'instructions',
            'ingredients',
            'is_veggie',
            'is_vegan'
        )
        extra_kwargs = {'ingredients': {'required': False}}


class CreateRecipeSerializer(serializers.ModelSerializer):
    """Handle the recipes creation."""

    name = serializers.CharField(
        validators= [UniqueValidator(
            queryset = Recipe.objects.all(),
            message = "This recipe was already created.")],
    )
    slug_name = serializers.CharField(
        validators= [UniqueValidator(
            queryset = Recipe.objects.all(),
            message = "This slug name was already used.")],
    )
    created_by = serializers.StringRelatedField() 


    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'slug_name',
            'created_by',
            'picture',
            'description',
            'instructions',
            'ingredients',
            'is_veggie',
            'is_vegan'
            )

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        return super().create(validated_data)