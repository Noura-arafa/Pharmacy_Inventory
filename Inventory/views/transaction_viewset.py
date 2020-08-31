from rest_framework import viewsets, filters, pagination, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from Inventory.models import Transaction
from Inventory.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    search_fields = ('quantity', 'transaction_data', 'transaction_type',)
    filterset_fields = ['quantity', 'transaction_data', 'transaction_type']

    def get_queryset(self):
        pagination.PageNumberPagination.page_size = self.request.query_params.get('size')
        return Transaction.objects.all()
