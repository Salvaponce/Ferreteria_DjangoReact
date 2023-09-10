from django.shortcuts import render
from core.models import Product, Cart, CustomUser
from django.contrib.auth.models import User
from core.serializers import (
    ProductSerializer,
    UserSerializer,
    CartSerializer,
)
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.reverse import reverse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def front(request):
    context = {}
    return render(request, "index.html", context)


# Funciona igual pero es mucho mas corto
class Product_List(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Product_Detalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetalle(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Cart(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [
        permissions.IsAdminUser,
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "products": reverse("products-list", request=request, format=format),
        }
    )


# En tu archivo views.py dentro de la aplicación de autenticación


@api_view(["POST"])
def user_register(request):
    """
    Vista para registrar un nuevo usuario.
    """
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {
                    "error": "Se requieren tanto un nombre de usuario como una contraseña."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Crea un nuevo usuario o maneja el caso si ya existe
        user, created = CustomUser.objects.get_or_create(username=username)
        user.set_password(password)
        user.save()

        # Genera un token de acceso para el usuario registrado
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def user_login(request):
    """
    Vista para iniciar sesión de un usuario y obtener un token de acceso.
    """
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {
                    "error": "Se requieren tanto un nombre de usuario como una contraseña."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Credenciales inválidas."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_logout(request):
    """
    Vista para cerrar sesión de un usuario.
    """
    if request.method == "POST":
        logout(request)
        return Response(
            {"message": "Sesión cerrada exitosamente."}, status=status.HTTP_200_OK
        )
