from django.urls import include, path, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from farms.api import views as farm_views

router = DefaultRouter()
router.register(r'farms', farm_views.FarmViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]