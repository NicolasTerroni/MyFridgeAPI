"""Recipes views."""

# Django REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from apps.recipes.serializers import RecipeModelSerializer, CreateRecipeSerializer

# Models
from apps.recipes.models import Recipe

# Permissions
from rest_framework.permissions import IsAuthenticated
from apps.recipes.permissions import IsRecipeOwner

# Utilities
from collections import Counter


class RecipesViewSet(ModelViewSet):
    """Recipes viewset."""

    queryset = Recipe.objects.all()
    lookup_field = 'slug_name'
    
    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated,]
        if self.action in ['update','partial_update','destroy']:
            permissions.append(IsRecipeOwner)
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        """Return serializer class based on action."""
        if self.action == "create":
            return CreateRecipeSerializer
        else:
            return RecipeModelSerializer

    @action(detail=False)
    def possible_recipes(self, request):
        """Returns recipes that contain at least one of the ingredients from the user's fridge."""
        
        # Get user fridge's ingredients
        fridge_ingredients_queryset = request.user.fridge.ingredients.all()
        # Transform the queryset into a list
        fridge_ingredients = [i for i in fridge_ingredients_queryset]

        # Get recipes that contain at least one of the ingredients from the user's fridge
        queryset = Recipe.objects.filter(ingredients__in=fridge_ingredients)
        # This will append to the queryset a recipe instance for each ingredient that matches.
        # Now order by most repeated recipes in the queryset and remove the repeated recipe instances.
        counts = Counter(queryset)
        queryset = sorted(counts, key=counts.get, reverse=True)
        
        # Pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
