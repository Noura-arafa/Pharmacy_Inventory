from rest_framework import serializers

from Inventory.models import DrugType


class DrugTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugType
        fields = '__all__'
        read_only_fields = ['id']
