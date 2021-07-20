"""Recipes views."""

# Django REST Framework
from rest_framework.viewsets import ModelViewSet

# Serializers
from apps.recipes.serializers import RecipeModelSerializer, CreateRecipeSerializer

# Models
from apps.recipes.models import Recipe

# Permissions
from rest_framework.permissions import IsAuthenticated
from apps.recipes.permissions import IsRecipeOwner


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