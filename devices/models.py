from django.db import models
import uuid
import json


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=100, unique=True, null=False)
    perma_name = models.CharField(max_length=100, unique=True, null=False)
    prefix = models.CharField(max_length=100, unique=True, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.display_name


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=100, unique=True, null=False)
    perma_name = models.CharField(max_length=100, unique=True, null=False)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="devices")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.display_name


class Action(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, null=False)
    device = models.ForeignKey(Device, on_delete=models.PROTECT, related_name="actions")
    payload = models.JSONField(encoder=json.JSONEncoder, decoder=json.JSONDecoder)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("Action")
        verbose_name_plural = ("Actions")

    def __str__(self):
        return self.name
