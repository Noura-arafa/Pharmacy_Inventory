from django.db import models


class DrugType(models.Model):
    type = models.CharField(max_length=200, unique=True)
