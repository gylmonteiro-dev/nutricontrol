from rest_framework import serializers
from .models import ProductEntry, StockEntry
from registrations.serializers import ProductModelSerializer, PlaceModelSerializer, SupplierModelSerializer

class ProductyEntryModelSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer()
    total_value = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = ProductEntry
        fields = ["id", "product", "price", "amount", "total_value"]

    
    def get_total_value(self, instance):
        total = instance.price * instance.amount
        return total


class StockEntryModelSerializer(serializers.ModelSerializer):
    place  = PlaceModelSerializer()
    supplier = SupplierModelSerializer()
    list_products = ProductyEntryModelSerializer(many=True)
    total_value = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = StockEntry
        fields = ["id", "place", "supplier", "list_products", "total_value"]

    
    def get_total_value(self, instance):
        products = instance.list_products.all()

        total = 0
        for product in products:
            total += product.price * product.amount
        
        return total

    
