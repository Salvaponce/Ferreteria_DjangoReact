from django.shortcuts import render
from core.models import Product, Cart
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
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

"""class Product_List(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)"""


def front(request):
    context = {}
    return render(request, "index.html", context)


# Funciona igual pero es mucho mas corto
class Product_List(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# The create() method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request.


"""class Product_Detalle(APIView):
    def get_object(self, id):
        try:
            product = Product.objects.get(id)
        except Product.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
    
    def get(self, id, request):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, id, request):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, id, request):
        product = self.get_object(id)
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)"""


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
