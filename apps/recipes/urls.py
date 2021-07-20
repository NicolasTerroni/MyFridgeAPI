"""Recipes urls"""
# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import recipes as recipes_views

router = DefaultRouter()
router.register(r'recipes',recipes_views.RecipesViewSet, basename='recipes')

urlpatterns = [
    path('',include(router.urls))
]
