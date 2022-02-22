from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Item, Order, Cart, Category, Menu
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token

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
    class Meta:
        model= Cart 
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    created_ts = serializers.ReadOnlyField()
    updated_ts = serializers.ReadOnlyField()
    class Meta:
        model = Order
        fields='__all__'




