from rest_framework import serializers

from .models import Brand, Device, Action

from thefuzz import process


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ("id", "display_name", "prefix", "created_at", "updated_at", "user")

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

    class Meta:
        model = Device
        fields = (
            "id",
            "display_name",
            "parent_brand",
            "created_at",
            "updated_at",
            "user",
        )


class ActionSerializer(serializers.ModelSerializer):

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
        )
