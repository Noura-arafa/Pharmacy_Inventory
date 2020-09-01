from rest_framework import viewsets, pagination, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from Inventory.models import DrugType
from Inventory.serializers import DrugTypeSerializer


class DrugTypeViewSet(viewsets.ModelViewSet):
    queryset = DrugType.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ('type',)
    serializer_class = DrugTypeSerializer

    def get_queryset(self):
        pagination.PageNumberPagination.page_size = self.request.query_params.get('size')
        return DrugType.objects.all()
