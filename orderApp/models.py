from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.name

    class Meta:
        db_table = "fo_category"
        verbose_name = "Category"


class Item(models.Model):
    name = models.CharField(max_length=30, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    def __str__(self):
        return self.name

    class Meta:
        db_table = "fo_items"
        verbose_name = "items"

class Menu(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = "fo_cart"
        verbose_name = "Cart"


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    total =models.FloatField(blank=False, default=0)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    created_ts = models.DateTimeField("Created Date", auto_now_add=True)
    updated_ts = models.DateTimeField("Last Updated Date", auto_now=True)
    def __str__(self):
        return f'order: {self.created_ts.strftime("%b %d %y %I :%M %p")}'
    def __str__(self):
        return f'order: {self.updated_ts.strftime("%b %d %y %I :%M %p")}'

    class Meta:
        db_table = "fo_order"
        verbose_name = "orders"



