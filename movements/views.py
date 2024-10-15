from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ProductEntry, StockEntry
from .serializers import ProductyEntryModelSerializer, StockEntryModelSerializer
# Create your views here.

class ProductEntryLisctCreateApiView(ListCreateAPIView):
    queryset = ProductEntry.objects.all()
    serializer_class = ProductyEntryModelSerializer


class ProductEntryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = ProductEntry.objects.all()
    serializer_class = ProductyEntryModelSerializer


class StockEntryLisctCreateApiView(ListCreateAPIView):
    queryset = StockEntry.objects.all()
    serializer_class = StockEntryModelSerializer


class StockEntryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = StockEntry.objects.all()
    serializer_class = StockEntryModelSerializer
