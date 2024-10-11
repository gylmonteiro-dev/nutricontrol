from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user__username"]
