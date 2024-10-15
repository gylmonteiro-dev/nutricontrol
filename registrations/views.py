from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
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


class ProductRetrieveUpdateDestroyApiView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class PlaceListCreateApiView(ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceModelSerializer


class PlaceRetrieveUpdateDestroyApiView(RetrieveUpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceModelSerializer


class SupplierListCreateApiView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = PlaceModelSerializer


class SupplierRetrieveUpdateDestroyApiView(RetrieveUpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = PlaceModelSerializer
