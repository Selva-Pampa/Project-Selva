from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
