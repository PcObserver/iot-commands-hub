from rest_framework import serializers
from django.contrib.auth import password_validation
from django.db import transaction

from .models import User


class SignUpUserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "password",
            "password_confirmation",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        try:
            password_validation.validate_password(value, self.instance)
        except serializers.ValidationError as error:
            raise serializers.ValidationError(error.messages)

        return value

    def validate(self, data):
        password_confirmation = data.pop("password_confirmation", None)

        if data.get("password") != password_confirmation:
            raise serializers.ValidationError(
                "Password and its confirmation have different values"
            )

        return data

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop("password", None)

        user = self.Meta.model(**validated_data)

        if password is not None:
            user.set_password(password)

        user.save()

        return user
