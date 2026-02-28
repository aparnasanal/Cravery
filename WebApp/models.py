from django.db import models

# Create your models here.

class ContactDb(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Subject = models.CharField(max_length=200)
    Message = models.TextField()

class RegistrationDb(models.Model):
    Username = models.CharField(max_length=100, unique=True)
    Email = models.EmailField(max_length=100, unique=True)
    Password = models.CharField(max_length=100)
    C_Password = models.CharField(max_length=100)

class CartDb(models.Model):
    Username = models.CharField(max_length=100)
    Restaurant = models.CharField(max_length=100, null=True, blank=True)
    Dish_Name = models.CharField(max_length=100)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Total_Price = models.FloatField()
    Dish_Image = models.ImageField(upload_to="Cart Images", null=True, blank=True)
