from django.contrib import admin

# Register your models here.
from orderApp.models import Category, Item, Menu, Cart, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    list_filter = ("category",)
    search_fields = ("name",)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_filter = ("item", )

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "item", "quantity")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "cart", "total", "created_ts", "is_paid", "updated_ts")
    list_filter = ("user",)