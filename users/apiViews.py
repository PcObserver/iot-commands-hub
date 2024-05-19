from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from .serializers import (
    SignUpUserSerializer,
    UserSerializer,
    CustomTokenObtainPairSerializer,
)
from .models import User
from .filters import UserFilter


from devices.serializers import BrandSerializer, DeviceSerializer, ActionSerializer
from devices.models import Brand, Device, Action


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

    @action(detail=True, methods=["get"], serializer_class=BrandSerializer)
    def brands(self, request, pk=None):
        user = self.get_object()
        queryset = user.contributions.filter(
            polymorphic_ctype=ContentType.objects.get_for_model(Brand)
        )

        paginator = PageNumberPagination()
        paginator.page_size = settings.REST_FRAMEWORK.get("PAGE_SIZE")
        result_page = paginator.paginate_queryset(queryset, request)

        serializer = self.get_serializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

    @action(detail=True, methods=["get"], serializer_class=DeviceSerializer)
    def devices(self, request, pk=None):
        user = self.get_object()

        queryset = user.contributions.filter(
            polymorphic_ctype=ContentType.objects.get_for_model(Device)
        )

        paginator = PageNumberPagination()
        paginator.page_size = settings.REST_FRAMEWORK.get("PAGE_SIZE")
        result_page = paginator.paginate_queryset(queryset, request)

        serializer = self.get_serializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

    @action(detail=True, methods=["get"], serializer_class=ActionSerializer)
    def actions(self, request, pk=None):
        user = self.get_object()

        queryset = user.contributions.filter(
            polymorphic_ctype=ContentType.objects.get_for_model(Action)
        )

        paginator = PageNumberPagination()
        paginator.page_size = settings.REST_FRAMEWORK.get("PAGE_SIZE")
        result_page = paginator.paginate_queryset(queryset, request)

        serializer = self.get_serializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)
