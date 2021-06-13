# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword', **extraFields)

# from django.db import models

# class User(models.Model):
#     username = models.CharField(max_length=15)
#     password = models.CharField(max_length=50) # Obviamente hasheada
#     email = models.CharField(max_length=50)    
#     name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)

#     address = models.CharField(max_length=50)
#     birth_date = models.DateField()
#     sex = models.CharField(max_length=15) 

#     def __str__(self):
#         return self.name

