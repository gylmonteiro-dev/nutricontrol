from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ProductEntry, StockEntry
# Create your views here.

class ProductEntryLisctCreateApiView(ListCreateAPIView):
    queryset = ProductEntry.objects.all()
    serializer_class = None


class ProductEntryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = ProductEntry.objects.all()
    serializer_class = None


class StockEntryLisctCreateApiView(ListCreateAPIView):
    queryset = StockEntry.objects.all()
    serializer_class = None


class StockEntryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = StockEntry.objects.all()
    serializer_class = None
