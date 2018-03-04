from django.db import models


class Product(models.Model):
    name = models.CharField(null=True, blank=False, default='', max_length=50)
    description = models.TextField(null=False, blank=True, default='')
