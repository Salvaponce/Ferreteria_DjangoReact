from rest_framework import serializers
from core.models import Product, Cart
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=60)
    description = serializers.CharField(style={"base_template": "textarea.html"})
    image = serializers.ImageField(required=False, upload_to="product")
    stock = serializers.BooleanField(default=False)
    category = serializers.CharField(max_length=50, default="Otras")
    price = serializers.FloatField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.image = validated_data.get("image", instance.image)
        instance.stock = validated_data.get("stock", instance.stock)
        instance.category = validated_data.get("category", instance.category)
        instance.price = validated_data.get("price", instance.price)
        instance.save()
        return instance"""

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
