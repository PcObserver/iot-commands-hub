from rest_framework.viewsets import ModelViewSet
from django.db.models import Count, Q

from .models import Brand, Device, Action
from .serializers import BrandSerializer, DeviceSerializer, ActionSerializer
from .filters import BrandFilter, DeviceFilter, ActionFilter


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filterset_class = BrandFilter
    http_method_names = ["get", "patch"]

    def get_queryset(self):
        queryset = self.queryset.annotate(
            positive_reviews_count=Count("reviews", filter=Q(reviews__type=0))
        ).order_by("-positive_reviews_count")

        return queryset


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filterset_class = DeviceFilter
    http_method_names = ["get", "patch"]
    
    def get_queryset(self):
        queryset = self.queryset.annotate(
            positive_reviews_count=Count("reviews", filter=Q(reviews__type=0))
        ).order_by("-positive_reviews_count")

        return queryset


class ActionViewSet(ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    filterset_class = ActionFilter
    http_method_names = ["get", "patch"]
    
    def get_queryset(self):
        queryset = self.queryset.annotate(
            positive_reviews_count=Count("reviews", filter=Q(reviews__type=0))
        ).order_by("-positive_reviews_count")

        return queryset
