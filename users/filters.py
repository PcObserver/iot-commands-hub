from django_filters import FilterSet, filters
from django.db.models import Q

from .models import User


class UserFilter(FilterSet):
    email = filters.CharFilter(method="filter_email")
    name = filters.CharFilter(method="filter_name")

    def filter_email(self, queryset, name, value):
        return queryset.filter(Q(email__icontains=value))
    
    def filter_name(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value))

    class Meta:
        model = User
        fields = ["id", "email", "name"]