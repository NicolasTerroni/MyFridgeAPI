"""Fridge models"""

# Django
from django.db import models

# Utilities
from apps.utils.models import TimeStamp

# Models
from apps.fridges.models.conteins import Contein


class Fridge(TimeStamp):
    """
    Fridge model.
    
    Fridges are what contains user's ingredients,
    Depending on the ingredients that it contains, the corresponding recipes will be displayed.
    """
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='owner'
    )
    ingredients = models.ManyToManyField(
        "ingredients.Ingredient",
        related_name='fridge_ingredients',
        through='fridges.Contein',
        blank=True)

    def __str__(self):
        return f"{self.owner}'s fridge."