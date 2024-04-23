from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from .apiViews import SignUpView

drf_router = DefaultRouter()
drf_router.register(r"sign_up", SignUpView)

urlpatterns = [
    path("log_in/", TokenObtainPairView.as_view(), name="obtain_token"),
    path("log_in/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("log_out/", TokenBlacklistView.as_view(), name="log_out"),
    path("", include(drf_router.urls)),
]
