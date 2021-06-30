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
    # created_by = ... 
    picture = models.ImageField(
        upload_to='recipes/pictures', 
        blank=True, 
        null=True
    )
    description = models.TextField(blank=True, max_length=150)

    instructions = models.TextField(blank=True)

    ingredients = models.ManyToManyField("ingredients.Ingredient",related_name='recipe_ingredients')
    # How to save the ingredients amount?

    is_veggie = models.BooleanField(
        default=False,
        help_text='Recipes with ingredients that do not contain meat or derivatives.'
    )
    is_vegan = models.BooleanField(
        default=False,
        help_text='Recipes with ingredients that do not come from animals.'
    )

    # rating = ...
    
    def __str__(self):
        return self.name

"""
    gluten_free = models.BooleanField(
        default=True,
        help_text='Ingredients that are suitable for celiacs (gluten free).'
    )

    lactose_free = models.BooleanField(
        default=True,
        help_text='Ingredients that are lactose free.'
    )
"""