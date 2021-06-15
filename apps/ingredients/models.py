"""Ingredients models"""

# Django
from django.db import models

# Utilities
from apps.utils.models import TimeStamp

class Ingredient(TimeStamp):
    """
    Ingredients model.
    
    Ingredients are the elements of our recipes,
    and also what our fridge contains.
    """

    name = models.CharField(unique=True, max_length=50)
    picture = models.ImageField(blank=True, null=True)
    description = models.TextField()

    is_veggie = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)

    def __str__(self):
        return self.name