from rest_framework import serializers
from core.models import Producto, Carrito, Notes
from django.contrib.auth.models import User


class ProductoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=60)
    descripcion = serializers.CharField(style={"base_template": "textarea.html"})
    imagen = serializers.CharField(max_length=150, allow_blank=True)
    stock = serializers.BooleanField(default=False)
    categoria = serializers.CharField(max_length=50, default="Otras")

    def create(self, validated_data):
        return Producto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.descripcion = validated_data.get("descripcion", instance.descripcion)
        instance.imagen = validated_data.get("imagen", instance.imagen)
        instance.stock = validated_data.get("stock", instance.stock)
        instance.categoria = validated_data.get("categoria", instance.categoria)
        instance.save()
        return instance

    class Meta:
        model = Producto
        fields = ["id", "name", "descripcion", "imagen", "stock", "categoria"]


class UserSerializer(serializers.ModelSerializer):
    productos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Producto.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "productos"]


class CarritoSerializer(serializers.ModelSerializer):
    productos = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Carrito
        fields = ("id", "owner", "producto", "cantidad")


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ("id", "title", "content")
