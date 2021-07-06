"""Ingredients views."""

# Django REST Framework
from rest_framework.viewsets import ModelViewSet

# Serializers
from apps.ingredients.serializers.ingredients import IngredientModelSerializer, CreateIngredientSerializer

# Models
from apps.ingredients.models import Ingredient

# Permissions
from rest_framework.permissions import IsAuthenticated
from apps.ingredients.permissions import IsIngredientOwner


class IngredientsViewSet(ModelViewSet):
    """Ingredients viewset."""

    queryset = Ingredient.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated,]
        if self.action in ['update','partial_update','delete']:
            permissions.append(IsIngredientOwner)
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        """Return serializer class based on action."""
        if self.action == "create":
            return CreateIngredientSerializer
        else:
            return IngredientModelSerializer

