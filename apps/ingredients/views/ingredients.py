"""Ingredients views."""

# Django REST Framework
from rest_framework.viewsets import ModelViewSet

# Serializers
from apps.ingredients.serializers.ingredients import IngredientModelSerializer 

# Models
from apps.ingredients.models import Ingredient

# Permissions
from rest_framework.permissions import IsAuthenticated
from apps.ingredients.permissions import IsIngredientOwner

class IngredientsViewSet(ModelViewSet):
    """Ingredients viewset."""

    queryset = Ingredient.objects.all()
    serializer_class = IngredientModelSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated,]
        if self.action in ['update','partial_update']:
            permissions.append(IsIngredientOwner)
        return [permission() for permission in permissions]