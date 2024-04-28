from django.db import models
import json

from contributions.models import Contribution


class Brand(Contribution):
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


class Device(Contribution):
    display_name = models.CharField(max_length=100, unique=True, null=False)
    perma_name = models.CharField(max_length=100, unique=True, null=False)
    parent_brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="devices")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.display_name


class Action(Contribution):
    name = models.CharField(max_length=100, unique=True, null=False)
    parent_device = models.ForeignKey(Device, on_delete=models.PROTECT, related_name="actions")
    payload = models.JSONField(encoder=json.JSONEncoder, decoder=json.JSONDecoder)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Action")
        verbose_name_plural = ("Actions")

    def __str__(self):
        return self.name
