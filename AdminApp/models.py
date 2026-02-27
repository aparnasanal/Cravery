from django.db import models

# Create your models here.

class CategoryDb(models.Model):
    CategoryName = models.CharField(max_length=100, unique=True)
    Description = models.TextField()
    CategoryImage = models.ImageField(upload_to="categories")

class RestaurantDb(models.Model):
    RestaurantName = models.CharField(max_length=100, unique=True)
    RestaurantPlace = models.CharField(max_length=100)
    RestDescription = models.TextField()
    RestaurantImage = models.ImageField(upload_to="restaurants")

class DishDb(models.Model):
    DishName = models.CharField(max_length=100)
    Category_Name = models.CharField(max_length=100)
    Restaurant_Name = models.CharField(max_length=100)
    DishPrice = models.IntegerField(null=True, blank=True)
    DishDescription = models.TextField()
    DishImage = models.ImageField(upload_to="dishes")