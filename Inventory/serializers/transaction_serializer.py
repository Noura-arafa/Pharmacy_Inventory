from rest_framework import serializers

from Inventory.models import Transaction, Item
from Inventory.serializers import ItemMinimizedSerializer


class TransactionSerializer(serializers.ModelSerializer):
    item = ItemMinimizedSerializer(read_only=True, required=False)
    item_id = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all, source='item')

    class Meta:
        model = Transaction
        fields = ['id',
                  'quantity',
                  'transaction_data',
                  'transaction_type',
                  'item',
                  'item_id']
