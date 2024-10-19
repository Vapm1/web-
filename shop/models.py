from django.db import models


# Create your models here
class Product(models.Model):
    title = models.CharField(max_length=16)
    price = models.PositiveIntegerField()
    description = models.TextField()
    when_added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/products/')
    discount = models.PositiveSmallIntegerField()
    stock = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    brand = models.CharField(max_length=32)