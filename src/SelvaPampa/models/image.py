from django.db import models

from .item import Item


class Image(models.Model):
    url = models.TextField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
