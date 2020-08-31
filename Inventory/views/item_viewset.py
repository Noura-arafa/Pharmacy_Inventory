from rest_framework import viewsets, filters, pagination, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from Inventory.models import Item
from Inventory.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def get_queryset(self):
        pagination.PageNumberPagination.page_size = self.request.query_params.get('size')
        return Item.objects.all()
