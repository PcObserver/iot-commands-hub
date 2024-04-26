

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apiViews import ContributionViewSet, ContributionReviewViewSet

drf_router = DefaultRouter()
drf_router.register(r"contribution_reviews", ContributionReviewViewSet)
drf_router.register(r"", ContributionViewSet)

urlpatterns = [
    path("", include(drf_router.urls)),
]
