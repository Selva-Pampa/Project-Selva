from django.db import models

from SelvaPampa.models.enums import Material, Prod_type

class Substratum(models.Model):
    prod_type = models.IntegerField(choices=Prod_type.choices)
    material = models.IntegerField(choices=Material.choices)
    color = models.CharField(max_length=20)
    # brand = enum

