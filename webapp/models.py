from django.db import models

# Create your models here.

class Registrationdb(models.Model):
    User_Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Profile_Image = models.ImageField(upload_to="registrationimages", null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class Contactusdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=200, null=True, blank=True)


class Cartdb(models.Model):
    User_Name = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=300, null=True, blank=True)
    Total_Price = models.IntegerField(null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Category_Name = models.CharField(max_length=100, null=True, blank=True)


class CheckoutDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=300, null=True, blank=True)








