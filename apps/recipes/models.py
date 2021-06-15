"""Recipes models"""

# Django
from django.db import models

# Utilities
from apps.utils.models import TimeStamp

class Recipe(TimeStamp):
    """
    Recipes model.
    
    Recipes are a set of instructions to prepare a meal,
    they contain a list of ingredients.
    """

    name = models.CharField(unique=True, max_length=50)
    picture = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, max_length=150)

    instructions = models.TextField(blank=True)

    ingredients = models.ManyToManyField("ingredients.Ingredient",related_name='ingredients')

    is_veggie = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)

    def __str__(self):
        return self.name