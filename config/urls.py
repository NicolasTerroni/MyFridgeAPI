"""MyFridgeApp URL Configuration """

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    
    path('',include(('apps.users.urls','users'), namespace='users')),
    path('',include(('apps.ingredients.urls','ingredients'), namespace='ingredients')),
    path('',include(('apps.fridges.urls','fridges'), namespace='fridges')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
