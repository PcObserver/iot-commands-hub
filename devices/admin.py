from django.contrib import admin

from .models import Brand, Device, Action

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_name', 'perma_name', 'prefix',)

    
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_name', 'perma_name', 'brand',)

    
@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'device',)    
