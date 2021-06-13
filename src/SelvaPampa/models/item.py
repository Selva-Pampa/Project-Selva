from django.db import models
# from django.contrib.postgres.fields import ArrayField
from SelvaPampa.models.design import Design
from SelvaPampa.models.substratum import Substratum

class Item(models.Model):
    name = models.CharField(max_length=12)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    substratum = models.ForeignKey(Substratum, on_delete=models.CASCADE)
    design = models.ForeignKey(Design,on_delete=models.CASCADE) 
    # pics = ArrayField(models.CharField(max_length=200))

    def __str__(self):
        return self.name