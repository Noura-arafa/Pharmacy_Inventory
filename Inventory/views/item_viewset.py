from rest_framework import viewsets, pagination, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
import rest_framework_filters
from rest_framework.response import Response
from rest_framework_filters.backends import DjangoFilterBackend

from Inventory.models import Item, Stock
from Inventory.serializers import ItemSerializer


class ItemFilter(rest_framework_filters.FilterSet):
    class Meta:
        model = Item
        fields = {
            'name': ('exact',),
            'barcode': ('exact',),
            'type': ('exact',),
            'date_created': ('exact',),
        }


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    search_fields = ('name',)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = ItemFilter

    def get_queryset(self):
        pagination.PageNumberPagination.page_size = self.request.query_params.get('size')
        return Item.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        item_stock = Stock.objects.filter(item_id=serializer.data['id'])
        serializer._data['quantity'] = item_stock.first().quantity if item_stock else 'out of stock'
        serializer._data['type_name'] = serializer.data['type']['type']
        print(serializer.data)
        return Response(serializer.data)

