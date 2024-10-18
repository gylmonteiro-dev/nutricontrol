from rest_framework import serializers
from .models import ProductEntry, StockEntry, StockOut
from registrations.models import Product
from registrations.serializers import ProductModelSerializer, PlaceModelSerializer, SupplierModelSerializer



class ProductEntryModelSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    product = ProductModelSerializer(read_only=True)
    total_value = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ProductEntry
        fields = [
            "id",
            "product",
            "product_id",
            "price",
            "amount",
            "total_value",
        ]

    def create(self, validated_data):
        product_id = validated_data.pop("product_id")
        product = Product.objects.get(pk=product_id)
        validated_data["product"] = product
        return super().create(validated_data)

    def get_total_value(self, instance):
        total = instance.price * instance.amount
        return total


class StockEntryModelSerializer(serializers.ModelSerializer):
    place  = PlaceModelSerializer()
    supplier = SupplierModelSerializer()
    list_products = ProductEntryModelSerializer(many=True)
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
