from rest_framework import serializers

from .models import Brand, Device, Action
from users.serializers import UserSerializer


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
            "user",
        )

    def get_devices_count(self, obj):
        return obj.devices.count()

    def get_positive_reviews_count(self, obj):
        return obj.reviews.filter(type=0).count()
    
    def to_representation(self, instance):
        representation = super(BrandSerializer, self).to_representation(instance)

        representation["user"] = (
            UserSerializer(instance.user).data
            if representation["user"] is not None
            else None
        )

        return representation
    
    def validate_display_name(self, value):
        user = self.context['request'].user

        existing_user_brands = Brand.objects.filter(display_name=value, user=user)

        if existing_user_brands:
            raise serializers.ValidationError("Current user already created a Brand with provided display_name")
        return value


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
            "actions_count",
            "positive_reviews_count",
            "user",
        )

    def get_actions_count(self, obj):
        return obj.actions.count()

    def get_positive_reviews_count(self, obj):
        return obj.reviews.filter(type=0).count()
    
    def to_representation(self, instance):
        representation = super(DeviceSerializer, self).to_representation(instance)

        representation["user"] = (
            UserSerializer(instance.user).data
            if representation["user"] is not None
            else None
        )

        return representation

    def validate_display_name(self, value):
        user = self.context['request'].user

        existing_user_brands = Brand.objects.filter(display_name=value, user=user)

        if existing_user_brands:
            raise serializers.ValidationError("Current user already created a Device with provided display_name")
        return value

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
    
    def to_representation(self, instance):
        representation = super(ActionSerializer, self).to_representation(instance)

        representation["user"] = (
            UserSerializer(instance.user).data
            if representation["user"] is not None
            else None
        )

        return representation
    
    def validate_display_name(self, value):
        user = self.context['request'].user

        existing_user_brands = Brand.objects.filter(display_name=value, user=user)

        if existing_user_brands:
            raise serializers.ValidationError("Current user already created an Action with provided name")
        return value
