from django.db import models


# Create your models here
class Product(models.Model):
    title = models.CharField(max_length=56)
    price = models.PositiveIntegerField()
    description = models.TextField()
    when_added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/products/')
    discount = models.PositiveSmallIntegerField()
    stock = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    brand = models.CharField(max_length=32)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    adres = models.CharField(max_length=52)
    email = models.EmailField()
    bank_card = models.CharField(max_length=16)
    count = models.PositiveIntegerField(default=1)