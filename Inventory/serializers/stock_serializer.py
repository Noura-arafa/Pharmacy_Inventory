from rest_framework import serializers

from Inventory.models import Stock
from Inventory.serializers import ItemMinimizedSerializer


class StockSerializer(serializers.ModelSerializer):
    item = ItemMinimizedSerializer(read_only=True, required=False)

    class Meta:
        model = Stock
        fields = ['id', 'item', 'quantity']
        read_only_fields = ['id']

