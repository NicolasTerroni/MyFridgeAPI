"""Fridges serializers."""

# Models
from apps.fridges.models import Fridge
from apps.users.models import User

# Django REST Framework
from rest_framework import serializers

# Serializers


class FridgeModelSerializer(serializers.ModelSerializer):
    """Fridge model serializer."""
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        """Meta class"""
        model = Fridge
        fields = ('owner','ingredients')
        extra_kwargs = {'ingredients': {'required': False}}