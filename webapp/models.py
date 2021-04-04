from django.db import models

# Create your models here.
class country(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=100)

    class Meta:
        db_table = "country"

    def __str__(self):  # this function will help me to get every value that we will store inside user table
        return self.cname

class states(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=100)
    c = models.ForeignKey(country,on_delete=models.CASCADE)

    class Meta:
        db_table = "states"

    def __str__(self):  # this function will help me to get every value that we will store inside user table
        return self.sname

class districts(models.Model):
    id = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=100)
    s = models.ForeignKey(states,on_delete=models.CASCADE)

    class Meta:
        db_table = "districts"

    def __str__(self):  # this function will help me to get every value that we will store inside user table
        return self.dname

class block(models.Model):
    id = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=100)
    district = models.ForeignKey(districts,on_delete=models.CASCADE)

    class Meta:
        db_table = "block"

    def __str__(self):  # this function will help me to get every value that we will store inside user table
        return self.bname

class village(models.Model):
    id = models.AutoField(primary_key=True)
    vname = models.CharField(max_length=100)
    block = models.ForeignKey(block,on_delete=models.CASCADE)

    class Meta:
        db_table = "village"

    def __str__(self):  # this function will help me to get every value that we will store inside user table
        return self.vname

class user(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100,default='Admin',editable=False)
    pwd = models.CharField(max_length=80)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pin = models.IntegerField(default=700084)

    class Meta:
        db_table = "user"

    def __str__(self):  # this function will help me to get every value that we will store inside user table
        return self.name

class funding_agency(models.Model):
    id = models.AutoField(primary_key=True)
    faname = models.CharField(max_length=100)
    u = models.ForeignKey(user,on_delete=models.CASCADE)

    class Meta:
        db_table = "funding_agency"

    def __str__(self):  # this function will help me to get every value that we will store inside user table
        return self.faname



#device - Aishani, devicelog, faultcode - Ashish , userdevice - Sharika