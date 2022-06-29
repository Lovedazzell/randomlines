from django.db import models

# Create your models here.

class Contactus(models.Model):
    name = models.CharField( max_length=30, null=False)
    email = models.EmailField(  max_length=30 ,null=False)
    number = models.IntegerField(  max_length=30, null=True)
    message = models.TextField(  max_length=150, null=False)
    