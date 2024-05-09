from rest_framework.viewsets import ModelViewSet

from .models import Brand, Device, Action
from .serializers import BrandSerializer, DeviceSerializer, ActionSerializer
from .filters import BrandFilter, DeviceFilter, ActionFilter


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filterset_class = BrandFilter
    http_method_names = ["get"]


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filterset_class = DeviceFilter
    http_method_names = ["get"]


class ActionViewSet(ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    filterset_class = ActionFilter
    http_method_names = ["get"]