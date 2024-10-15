from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Place, Product, Supplier
# Create your views here.


class ProductListCreateApiView(ListCreateAPIView):
    queryset = Product.objects.all
    serializer_class =  None


class ProductRetrieveUpdateDestroyApiView(RetrieveUpdateAPIView):
    queryset = Product.objects.all
    serializer_class = None


class PlaceListCreateApiView(ListCreateAPIView):
    queryset = Place.objects.all
    serializer_class = None


class PlaceRetrieveUpdateDestroyApiView(RetrieveUpdateAPIView):
    queryset = Place.objects.all
    serializer_class = None


class SupplierListCreateApiView(ListCreateAPIView):
    queryset = Supplier.objects.all
    serializer_class = None


class SupplierRetrieveUpdateDestroyApiView(RetrieveUpdateAPIView):
    queryset = Supplier.objects.all
    serializer_class = None
