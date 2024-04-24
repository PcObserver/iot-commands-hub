from rest_framework.viewsets import ModelViewSet

from .models import Brand, Device, Action
from .serializers import BrandSerializer, DeviceSerializer, ActionSerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    http_method_names = ["get"]


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    http_method_names = ["get"]


class ActionViewSet(ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    http_method_names = ["get"]