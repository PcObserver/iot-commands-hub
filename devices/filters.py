from django_filters import FilterSet, filters
from django.db.models import Q
from thefuzz import process

from .models import Brand, Device, Action


class BrandFilter(FilterSet):
    display_name = filters.CharFilter(method="filter_display_name")
    prefix = filters.CharFilter()
    similar_display_name = filters.CharFilter(
        method="filter_similar_name", label="Similar Name"
    )

    def filter_display_name(self, queryset, name, value):
        return queryset.filter(Q(display_name__icontains=value))

    def filter_similar_name(self, queryset, name, value):
        brand_names = Brand.objects.values_list("display_name", flat=True)
        minimal_match_score = 60

        best_matches = process.extractBests(
            value, brand_names, score_cutoff=minimal_match_score
        )
        similar_names = [similar_name[0] for similar_name in best_matches]

        return queryset.filter(Q(display_name__in=similar_names))

    class Meta:
        model = Brand
        fields = [
            "id",
            "display_name",
            "prefix",
            "similar_display_name",
        ]


class DeviceFilter(FilterSet):
    display_name = filters.CharFilter(method="filter_display_name")
    similar_display_name = filters.CharFilter(
        method="filter_similar_name", label="Similar Name"
    )
    parent_brand = filters.UUIDFilter(field_name="parent_brand__id")

    def filter_display_name(self, queryset, name, value):
        return queryset.filter(Q(display_name__icontains=value))

    def filter_similar_name(self, queryset, name, value):
        device_names = Device.objects.values_list("display_name", flat=True)
        minimal_match_score = 60

        best_matches = process.extractBests(
            value, device_names, score_cutoff=minimal_match_score
        )
        similar_names = [similar_name[0] for similar_name in best_matches]

        return queryset.filter(Q(display_name__in=similar_names))

    class Meta:
        model = Device
        fields = ["id", "display_name", "parent_brand", "similar_display_name"]


class ActionFilter(FilterSet):
    name = filters.CharFilter(method="filter_name")
    similar_name = filters.CharFilter(
        method="filter_similar_name", label="Similar Name"
    )
    parent_device = filters.UUIDFilter(field_name="parent_device__id")

    def filter_name(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value))

    def filter_similar_name(self, queryset, name, value):
        device_names = Action.objects.values_list("display_name", flat=True)
        minimal_match_score = 60

        best_matches = process.extractBests(
            value, device_names, score_cutoff=minimal_match_score
        )
        similar_names = [similar_name[0] for similar_name in best_matches]

        return queryset.filter(Q(display_name__in=similar_names))

    class Meta:
        model = Action
        fields = ["id", "name", "parent_device", "similar_name"]
