from rest_framework import serializers
from .models import Place, Product, Profile, Supplier


class PlaceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = "__all__"


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProfileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"


class SupplierModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = "__all__"
