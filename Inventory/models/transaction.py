from django.db import models

from Inventory.models import Item


class Transaction(models.Model):
    item = models.ForeignKey(Item, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=True, blank=True)  # num of items
    transaction_data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    transaction_type = models.IntegerField()  # 0--> neg transaction  1--> pos transaction
