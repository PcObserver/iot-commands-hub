from rest_framework import serializers

from .models import Brand, Device, Action
from users.serializers import UserSerializer

from thefuzz import process


class BrandSerializer(serializers.ModelSerializer):
    devices_count = serializers.SerializerMethodField()
    positive_reviews_count = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

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
            "user",
        )

    def get_devices_count(self, obj):
        return obj.devices.count()

    def get_positive_reviews_count(self, obj):
        return obj.reviews.filter(type=0).count()

    def validate_display_names(self, value):
        brand_names = Brand.objects.values_list("display_name", flat=True)
        minimal_match_score = 90

        similar_name = process.extractOne(value, brand_names, scorer_cutoff=minimal_match_score)

        if similar_name:
            raise serializers.ValidationError(
                "There's a Brand with a similar name with the one provided"
            )

        return value


class DeviceSerializer(serializers.ModelSerializer):
    actions_count = serializers.SerializerMethodField()
    positive_reviews_count = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Device
        fields = (
            "id",
            "display_name",
            "parent_brand",
            "created_at",
            "updated_at",
            "actions_count",
            "positive_reviews_count",
            "user",
        )

    def get_actions_count(self, obj):
        return obj.actions.count()

    def get_positive_reviews_count(self, obj):
        return obj.reviews.filter(type=0).count()


class ActionSerializer(serializers.ModelSerializer):
    positive_reviews_count = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Action
        fields = (
            "id",
            "name",
            "parent_device",
            "payload",
            "created_at",
            "updated_at",
            "positive_reviews_count",
            "user",
            "method",
            "protocol",
            "path",
        )

    def get_positive_reviews_count(self, obj):
        return obj.reviews.filter(type=0).count()
    
    def validate(self, data):
        if not data.get("path"):
            raise serializers.ValidationError("Needs to define the device action's path")

        return data
