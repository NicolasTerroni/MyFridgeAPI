"""Profile model"""

# Django
from django.db import models

# Models
from apps.users.models.users import User

# Utilities
from apps.utils.models import TimeStamp


class Profile(TimeStamp, models.Model):
    """Users profile model"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    picture = models.ImageField(
        upload_to='profiles/pictures', 
        blank=True, 
        null=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    biography = models.TextField(max_length=500,blank=True)

    # Stats
    # created_recipes = ...
    # created_ingredients = ...
    # favourite_recipes = ...
    

    def __str__(self):
        return str(self.user)