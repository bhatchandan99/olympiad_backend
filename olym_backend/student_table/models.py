from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
from passlib.hash import pbkdf2_sha256



class Student(AbstractUser):
    id=models.AutoField(primary_key=True)
    name = models.CharField(null=False,max_length=100)
    ref_code = models.CharField(blank=True,max_length=20)
    parent_name = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    country = CountryField()
    address = models.CharField(null=True,max_length=100)
    school=models.CharField(max_length=100)
    school_state = models.CharField(max_length=100)
    school_address=models.CharField(max_length=100)
    school_city=models.CharField(max_length=100)
    pincode = models.IntegerField(null = True)
    number=models.IntegerField(null=True)
    standard = models.CharField(null=True,max_length=10,default=1)

    def __str__(self):
        return str(self.id)

    def verify_password(self,raw_password):


        return pbkdf2_sha256.verify(raw_password,self.password)


# Create your models here.
