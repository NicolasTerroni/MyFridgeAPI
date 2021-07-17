"""Ingredients permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission

class IsIngredientOwner(BasePermission):
    """Allow access only to objects owned by the requesting user."""

    def has_object_permission(self,request,view,obj):
        """Check out if object creator and user are the same."""
        if not obj.created_by:
            return False
        return request.user == obj.created_by