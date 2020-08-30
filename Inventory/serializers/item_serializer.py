from rest_framework import serializers

from Inventory.models import Item, DrugType
from Inventory.serializers import DrugTypeSerializer


class ItemSerializer(serializers.ModelSerializer):
    type_id = serializers.PrimaryKeyRelatedField(queryset=DrugType.objects.all(), source='type', allow_null=True,
                                                 required=False)
    type = DrugTypeSerializer(read_only=True, required=False)

    class Meta:
        model = Item
        fields = [
            'id',
            'date_created',
            'name',
            'price',
            'description',
            'type',
            'type_id']
        read_only_fields = ['id']


class ItemMinimizedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'name'
        ]
