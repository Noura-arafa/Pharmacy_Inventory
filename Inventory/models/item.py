from django.db import models
import django_mysql.models

from Inventory.models import DrugType


class Item(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    name = models.CharField(max_length=200, unique=True)
    price = models.FloatField(null=True, blank=True)
    description = models.CharField(max_length=250, null=True)
    barcode = models.CharField(max_length=250, null=True)
    type = models.ForeignKey(DrugType, null=True, blank=True, on_delete=models.SET_NULL)  # Drug type
