# import enum
from django.db import models

class Prod_type(models.IntegerChoices):
    TAZA = 1
    GORRA = 2
    REMERA = 3

class Material(models.IntegerChoices): 
    CERAMICA = 1
    VIDRIO = 2
    PLASTICO = 3
    PAPEL = 4
    METAL = 5
    TELA = 6

# class brand(enum.Enum):
