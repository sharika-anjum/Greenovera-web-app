from django.db import models

# Create your models here.
class user(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    pwd = models.CharField(max_length=80)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=70)
    district = models.CharField(max_length=50)
    pin = models.IntegerField(default=700084)

    class Meta:
        db_table = "user"

    def __str__(self):  # this function will help me to get every value that we will store inside user table
        return self.name
