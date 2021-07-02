"""Ingredients urls"""
# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import ingredients as ing_views

router = DefaultRouter()
router.register(r'ingredients',ing_views.IngredientsViewSet, basename='ingredients')

urlpatterns = [
    path('',include(router.urls))
]
