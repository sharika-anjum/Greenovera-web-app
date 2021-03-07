from django.db import models

# Create your models here.
class User1(models.Model):
    name        = models.CharField(max_length=100)
    email       = models.EmailField(max_length=60,  unique=True)
    username    = models.CharField(max_length=10,   unique=True)
    password    = models.CharField(max_length=10,   unique=True)

    objects=models.Manager()