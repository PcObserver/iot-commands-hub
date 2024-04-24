from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from .models import Contribution

from devices.models import Brand, Device, Action
from devices.serializers import BrandSerializer, DeviceSerializer, ActionSerializer


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = "__all__"


class ContributionPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = 'contribution_type'
    model_serializer_mapping = {
        Contribution: ContributionSerializer,
        Brand: BrandSerializer,
        Device: DeviceSerializer,
        Action: ActionSerializer
    }
