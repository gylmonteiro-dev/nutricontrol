from rest_framework import serializers
from .models import ProductEntry, StockEntry, StockOut
from registrations.models import Product, Place
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


class StockOutModelSerializer(serializers.ModelSerializer):
    place_id = serializers.IntegerField(write_only=True)
    place = PlaceModelSerializer(read_only=True)
    list_products_ids = serializers.ListField(write_only=True)
    list_products = ProductEntryModelSerializer(many=True, read_only=True)
    total_value = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = StockOut
        fields = [
            "id",
            "place",
            "place_id",
            "output_type",
            "description",
            "list_products",
            "list_products_ids",
            "total_value",
        ]

    def create(self, validated_data):
        # Place
        place_id = validated_data.pop("place_id")
        place = Place.objects.get(pk=place_id)
        validated_data["place"] = place

        # List Products
        list_products_ids = validated_data.pop("list_products_ids")
        list_products = [ProductEntry.objects.get(pk=id) for  id in list_products_ids]
        validated_data["list_products"] = list_products
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if validated_data.get("list_products_ids"):
            list_products_ids = validated_data.pop("list_products_ids")
            list_products = [ProductEntry.objects.get(pk=id) for id in list_products_ids]
            validated_data["list_products"] = list_products
            return super().update(instance, validated_data)
        return super().update(instance, validated_data)

    def get_total_value(self, instance):
        products = instance.list_products.all()

        total = 0
        for product in products:
            total += product.price * product.amount

        return total
