"""Fridges serializers."""

# Models
from apps.fridges.models import Fridge

# Django REST Framework
from rest_framework import serializers


class FridgeModelSerializer(serializers.ModelSerializer):
    """Fridge model serializer."""

    class Meta:
        """Meta class"""
        model = Fridge
        fields = (
            'ingredients',
        )