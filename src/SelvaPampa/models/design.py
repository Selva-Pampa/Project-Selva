from django.db import models
from django.contrib.auth.models import User

class Design(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.CharField(max_length=200) # Url de la foto
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=50,default=None)
    
    color = models.CharField(max_length=20)
    theme = models.CharField(max_length=50)
    style = models.CharField(max_length=30)

    def __str__(self):
        return self.title
