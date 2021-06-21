from django.db import models
from .design import Design
from .substratum import Substratum


class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    substratum = models.ForeignKey(
        Substratum, on_delete=models.CASCADE, null=True)
    design = models.ForeignKey(Design, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
