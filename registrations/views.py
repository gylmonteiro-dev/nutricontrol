from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Place, Product, Supplier
from .serializers import (
    ProductModelSerializer,
    PlaceModelSerializer,
    SupplierModelSerializer,
)

# Create your views here.


class ProductListCreateApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class ProductRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class PlaceListCreateApiView(ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceModelSerializer


class PlaceRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceModelSerializer


class SupplierListCreateApiView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer


class SupplierRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer
