from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    SignUpUserSerializer,
    UserSerializer,
    CustomTokenObtainPairSerializer,
)
from .models import User
from .filters import UserFilter


class SignUpViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        AllowAny,
    ]
    serializer_class = SignUpUserSerializer
    http_method_names = ["post"]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    http_method_names = ["get", "patch"]
