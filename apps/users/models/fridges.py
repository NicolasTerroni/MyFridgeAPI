"""Fridge models"""

# Django
from django.db import models

# Models
from apps.users.models import User

# Utilities
from apps.utils.models import TimeStamp

class Fridge(TimeStamp):
    """
    Fridge model.
    
    Fridges are what contains user's ingredients,
    Depending on the ingredients that it contains, the corresponding recipes will be displayed.
    """
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    ingredients = models.ManyToManyField(
        "ingredients.Ingredient",
        related_name='ingredients',
        blank=True)

    def __str__(self):
        return f"{self.owner}'s fridge."