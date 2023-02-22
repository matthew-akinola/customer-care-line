import uuid
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class CustomUser(models.Model):
    company_id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True, 
        primary_key=True
        )
    company_name = models.CharField(max_length=20, null=True)
    Address = models.CharField(max_length=20, null=True)
    Email = models.EmailField()
    Phone_Number = PhoneNumberField()
    Country = CountryField()
    Password = models.CharField(
        max_length=20, 
        null=True
        )
    is_admin = models.BooleanField(default=True)

    def __repr__(self):
        return self.Company_name

class Helpline(models.Model):
    Phone_number = PhoneNumberField()
    Branch = models.CharField(max_length=500, null=True)
    City = models.CharField(max_length=500, null=True)
    Country = CountryField()

   



