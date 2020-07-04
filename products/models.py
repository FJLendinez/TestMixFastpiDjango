from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=150)
