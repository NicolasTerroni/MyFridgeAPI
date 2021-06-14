"""Profile model"""

# Django
from django.db import models

# Models
from apps.users.models.users import User

class Profile(models.Model):
    """Users profile model"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    biography = models.TextField(max_length=500,blank=True)

    # favourite_recipes = ...


    def __str__(self):
        return f'{self.first_name} {self.first_name}'