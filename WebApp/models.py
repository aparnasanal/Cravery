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
