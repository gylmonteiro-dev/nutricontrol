from django.contrib import admin
from .models import ProductEntry, StockEntry, StockOut

# Register your models here.


@admin.register(ProductEntry)
class ProductEntryAdmin(admin.ModelAdmin):
    list_display = ["id", "product"]


@admin.register(StockEntry)
class StockEntryAdmin(admin.ModelAdmin):
    list_display = ["id", "place", "created_at"]


@admin.register(StockOut)
class StockEntryAdmin(admin.ModelAdmin):
    list_display = ["id", "place","output_type", "created_at"]
