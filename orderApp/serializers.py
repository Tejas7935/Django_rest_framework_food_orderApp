from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Item, Order, Cart, Category, Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model= Menu
        fields='__all__'

class ItemSerializer(serializers.ModelSerializer):
    item = MenuSerializer(read_only=True, many=True)
    class Meta:
        model = Item
        fields= ['id', 'name', 'price', 'category', 'item']

class CategorySerializer(serializers.ModelSerializer):
    category = ItemSerializer(read_only=True, many=True)
    class Meta:
        model= Category
        fields='__all__'








class CartSerializer(serializers.ModelSerializer):
    # item = ItemSerializer()
    class Meta:
        model= Cart
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    # cart = CartSerializer()

    class Meta:
        model = Order
        fields='__all__'


