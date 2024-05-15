from rest_framework import serializers

from .models import Brand, Device, Action


class BrandSerializer(serializers.ModelSerializer):
    devices_count = serializers.SerializerMethodField()
    positive_reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = (
            "id",
            "display_name",
            "prefix",
            "created_at",
            "updated_at",
            "user",
            "devices_count",
            "positive_reviews_count",
        )

    def get_devices_count(self, obj):
        return obj.devices.count()

    def get_positive_reviews_count(self, obj):
        return obj.reviews.filter(type=0).count()


class DeviceSerializer(serializers.ModelSerializer):
    actions_count = serializers.SerializerMethodField()
    positive_reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Device
        fields = (
            "id",
            "display_name",
            "parent_brand",
            "created_at",
            "updated_at",
            "user",
            "actions_count",
            "positive_reviews_count",
        )

    def get_actions_count(self, obj):
        return obj.actions.count()

    def get_positive_reviews_count(self, obj):
        return obj.reviews.filter(type=0).count()


class ActionSerializer(serializers.ModelSerializer):
    positive_reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Action
        fields = (
            "id",
            "name",
            "parent_device",
            "payload",
            "created_at",
            "updated_at",
            "user",
            "positive_reviews_count",
        )

    def get_positive_reviews_count(self, obj):
        return obj.reviews.filter(type=0).count()
