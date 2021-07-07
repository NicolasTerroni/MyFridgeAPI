"""Fridges views"""

# Django REST Framework
from rest_framework import viewsets, mixins

# Serializers
from apps.fridges.serializers.fridges import FridgeModelSerializer

# Permissions
from rest_framework.permissions import IsAuthenticated
from apps.fridges.permissions import IsFridgeOwner


class FridgesViewSet(   viewsets.GenericViewSet, 
                        mixins.RetrieveModelMixin, 
                        mixins.UpdateModelMixin):
    """Fridges viewset."""
    permission_classes = [IsAuthenticated, IsFridgeOwner]
    serializer_class = FridgeModelSerializer