from django.shortcuts import get_object_or_404
from rest_framework import viewsets, pagination, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_filters.backends import DjangoFilterBackend
import rest_framework_filters as filters

from Inventory.models import Transaction, Stock
from Inventory.serializers import TransactionSerializer


class TransactionFilter(filters.FilterSet):
    class Meta:
        model = Transaction
        fields = {
            'transaction_type': ('exact',),
            'item__name': ('exact',),
            'quantity': ('exact',),
            'transaction_date': ('exact',),
        }


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_class = TransactionFilter
    pagination_class = PageNumberPagination

    def get_queryset(self):
        pagination.PageNumberPagination.page_size = self.request.query_params.get('size')
        return Transaction.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Calculate stock quantity
        item_stock = get_object_or_404(Stock, pk=serializer.validated_data['item'].id)
        if item_stock.quantity == 0 and serializer.validated_data['transaction_type'] == 0:
            return Response('out of stock', status=status.HTTP_200_OK)

        if serializer.validated_data['transaction_type'] == 1:
            item_stock.quantity += serializer.validated_data['quantity']
        else:
            item_stock.quantity -= serializer.validated_data['quantity']

        item_stock.save()
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
