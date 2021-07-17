"""Fridges serializers."""

# Models
from apps.users.models import Fridge

# Django REST Framework
from rest_framework import serializers

# Serializers


class FridgeModelSerializer(serializers.ModelSerializer):
    """Fridge model serializer."""

    class Meta:
        """Meta class"""
        model = Fridge
        fields = ('ingredients',)
        extra_kwargs = {'ingredients': {'required': False}}