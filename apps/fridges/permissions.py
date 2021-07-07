"""Fridge permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission

class IsFridgeOwner(BasePermission):
    """Allow access only to objects owned by the requesting user."""

    def has_object_permission(self,request,view,obj):
        """Check out if object and user are the same."""
        return request.user == obj.owner