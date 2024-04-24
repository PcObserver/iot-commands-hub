from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apiViews import BrandViewSet, DeviceViewSet, ActionViewSet

drf_router = DefaultRouter()
drf_router.register(r"brands", BrandViewSet)
drf_router.register(r"devices", DeviceViewSet)
drf_router.register(r"actions", ActionViewSet)

urlpatterns = [
    path("", include(drf_router.urls)),
]
