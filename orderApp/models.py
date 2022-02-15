from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=30, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    price = models.IntegerField()
    def __str__(self):
        return self.name


class Menu(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default="")


    def __str__(self):
        return self.item.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default="")
    item = models.ForeignKey(Item, on_delete=models.CASCADE , default="")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE , default="")
    is_paid = models.BooleanField()
    total =models.IntegerField(blank=False, default=0 )
    user  = models.ForeignKey(User, on_delete=models.CASCADE , default="")
    def __str__(self):
        return str(self.cart)


