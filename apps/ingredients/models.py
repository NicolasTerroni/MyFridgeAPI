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
    created_by = models.ForeignKey("users.User",on_delete=models.SET_NULL,null=True)
    picture = models.ImageField(
        upload_to='ingredients/pictures', 
        blank=True, 
        null=True
    )    
    description = models.TextField(blank=True)

    is_veggie = models.BooleanField(
        help_text='Ingredients that do not contain meat or derivatives.',
    )
    is_vegan = models.BooleanField(
        help_text='Ingredients that do not come from animals.',
    )

    # Maybe add booleans to classify them better, for example: dairy, fish, ...

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