from rest_framework import serializers

from .models import Brand, Device, Action


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ("id", "display_name", "perma_name", "prefix", "created_at", "updated_at", "user")


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ("id", "display_name", "perma_name", "parent_brand", "created_at", "updated_at", "user")


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = ("id", "name", "parent_device", "payload", "created_at", "updated_at", "user")
