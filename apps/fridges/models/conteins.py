"""Fridge contein model."""

# Django
from apps.fridges.models import fridges
from django.db import models

# Utilities
from apps.utils.models import TimeStamp

class Contein(TimeStamp):
    """
    Fridges contein model.

    This model stores the relation between a fridge and an ingredient.   
    """
    fridge = models.ForeignKey('fridges.Fridge', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        """Return ingredient and amount"""
        return f'{self.amount} {self.ingredient.name}'