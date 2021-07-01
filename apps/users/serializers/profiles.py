"""Profile serializers."""

# Models
from apps.users.models import Profile

# Django REST Framework
from rest_framework import serializers


class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""

    class Meta:
        """Meta class"""
        model = Profile
        fields = (
            'picture',
            'first_name',
            'last_name',
            'biography',
        )