from rest_framework import serializers
from core.models import Product, Cart, CustomUser
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(many=True, queryset=Cart.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "cart"]


class CartSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Cart
        fields = ("id", "owner", "product", "cantidad")


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "date_joined", "is_active", "is_staff")
