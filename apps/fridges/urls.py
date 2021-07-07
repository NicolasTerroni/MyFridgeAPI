"""Fridges urls"""
# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import fridges as fridges_views

router = DefaultRouter()
router.register(r'fridges',fridges_views.FridgesViewSet, basename='fridges')

urlpatterns = [
    path('',include(router.urls))
]
