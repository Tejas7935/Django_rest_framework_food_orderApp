from django.contrib import admin

# Register your models here.
from orderApp.models import Category, Item, Menu, Cart, Order

admin.site.register([Category, Item, Menu, Cart, Order])