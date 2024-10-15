from rest_framework import serializers
from .models import ProductEntry, StockEntry


class ProductyEntryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductEntry
        fields = "__all__"


class StockEntryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model =  StockEntry
        fields = "__all__"