from rest_framework import serializers

from Inventory.models import Stock, Item
from Inventory.serializers import ItemMinimizedSerializer


class StockSerializer(serializers.ModelSerializer):
    item = ItemMinimizedSerializer(read_only=True, required=False)
    item_id = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), source='item')

    class Meta:
        model = Stock
        fields = ['id', 'item', 'quantity', 'item_id']
        read_only_fields = ['id']

