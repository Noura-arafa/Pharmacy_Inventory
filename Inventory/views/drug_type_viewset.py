from rest_framework import viewsets, filters, pagination, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Inventory.models import DrugType
from Inventory.serializers import DrugTypeSerializer


class DrugTypeViewSet(viewsets.ModelViewSet):
    queryset = DrugType.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    search_fields = ('type',)
    filterset_fields = ['type']
    serializer_class = DrugTypeSerializer

    def get_queryset(self):
        pagination.PageNumberPagination.page_size = self.request.query_params.get('size')
        return DrugType.objects.all()
