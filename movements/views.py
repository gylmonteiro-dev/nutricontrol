from collections import defaultdict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ProductEntry, StockEntry, StockOut
from .serializers import ProductyEntryModelSerializer, StockEntryModelSerializer

# Create your views here.


class ProductEntryListCreateApiView(ListCreateAPIView):
    queryset = ProductEntry.objects.all()
    serializer_class = ProductyEntryModelSerializer


class ProductEntryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = ProductEntry.objects.all()
    serializer_class = ProductyEntryModelSerializer


class StockEntryListCreateApiView(ListCreateAPIView):
    queryset = StockEntry.objects.all()
    serializer_class = StockEntryModelSerializer


class StockEntryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = StockEntry.objects.all()
    serializer_class = StockEntryModelSerializer


class StockOutListCreateApiView(ListCreateAPIView):
    queryset = StockOut.objects.all()
    serializer_class = StockEntryModelSerializer


class StockOutRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = StockOut.objects.all()
    serializer_class = StockEntryModelSerializer


class StockView(APIView):
    
    def get(self, request, pk):
        stock_place = StockEntry.objects.filter(place__id = pk)
        all_entries = defaultdict(int)
        for stock in stock_place:
            for products in stock.list_products.all():
                all_entries[products.product.name] +=products.amount



        stock_out_place  = StockOut.objects.filter(place__id = pk)
        all_outs = defaultdict(int)
        for stock in stock_out_place:
            for products in stock.list_products.all():
                all_outs[products.product.name] += products.amount

        
        stock_current = defaultdict(int)
        for product, quantity_in in all_entries.items():
            quantity_out = all_outs.get(product, 0)
            
            stock_current[product] = quantity_in - quantity_out

        for product, quantity_out in all_outs.items():
            if product not in all_entries:
                stock_current[product]= -quantity_out

        return Response(stock_current, status=200)