from django_filters import FilterSet, filters
from django.db.models import Q

from .models import Brand, Device, Action


class BrandFilter(FilterSet):
    display_name = filters.CharFilter(method="filter_display_name")
    prefix = filters.CharFilter()

    def filter_display_name(self, queryset, name, value):
        return queryset.filter(Q(display_name__icontains=value))

    class Meta:
        model = Brand
        fields = ["id", "display_name", "prefix"]
        

class DeviceFilter(FilterSet):
    display_name = filters.CharFilter(method="filter_display_name")
    parent_brand = filters.UUIDFilter(field_name='parent_brand__id')

    def filter_display_name(self, queryset, name, value):
        return queryset.filter(Q(display_name__icontains=value))

    class Meta:
        model = Device
        fields = ["id", "display_name", "parent_brand"]
        
        
class ActionFilter(FilterSet):
    name = filters.CharFilter(method="filter_name")
    parent_device = filters.UUIDFilter(field_name='parent_device__id')

    def filter_name(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value))

    class Meta:
        model = Action
        fields = ["id", "name", "parent_device"]

