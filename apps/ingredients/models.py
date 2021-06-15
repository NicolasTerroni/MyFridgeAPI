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
    picture = models.ImageField(
        upload_to='ingredients/pictures', 
        blank=True, 
        null=True
    )    
    description = models.TextField()

    is_veggie = models.BooleanField(
        default=False,
        help_text='Ingredients that do not contain meat or derivatives.'
    )
    is_vegan = models.BooleanField(
        default=False,
        help_text='Ingredients that do not come from animals.'
    )

    def __str__(self):
        return self.name