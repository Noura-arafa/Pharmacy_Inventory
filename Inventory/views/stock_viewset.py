from rest_framework import viewsets, pagination
import rest_framework_filters as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_filters.backends import DjangoFilterBackend

from Inventory.models import Stock
from Inventory.serializers import StockSerializer


class StockFilter(filters.FilterSet):
    class Meta:
        model = Stock
        fields = {
            'item__name': ('exact',),
            'quantity': ('exact',),
        }


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    search_fields = ('quantity',)
    filter_backends = [DjangoFilterBackend]
    filter_class = StockFilter

    def get_queryset(self):
        pagination.PageNumberPagination.page_size = self.request.query_params.get('size')
        return Stock.objects.all()
