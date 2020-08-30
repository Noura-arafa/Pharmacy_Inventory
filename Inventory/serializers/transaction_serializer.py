from rest_framework import serializers

from Inventory.models import Transaction
from Inventory.serializers import ItemMinimizedSerializer


class TransactionSerializer(serializers.ModelSerializer):
    item = ItemMinimizedSerializer(read_only=True, required=False)

    class Meta:
        model = Transaction
        fields = ['id',
                  'quantity',
                  'transaction_data',
                  'transaction_type',
                  'item']
