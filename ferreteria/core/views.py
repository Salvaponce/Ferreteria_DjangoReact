from django.shortcuts import render
from core.models import Producto, Carrito, Notes
from django.contrib.auth.models import User
from core.serializers import (
    ProductoSerializer,
    UserSerializer,
    CarritoSerializer,
    NoteSerializer,
)
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

"""class Producto_List(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)"""


def front(request):
    context = {}
    return render(request, "index.html", context)

#Funciona igual pero es mucho mas corto
class Producto_List(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


# The create() method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request.


"""class Producto_Detalle(APIView):
    def get_object(self, id):
        try:
            producto = Producto.objects.get(id)
        except Producto.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
    
    def get(self, id, request):
        producto = self.get_object(id)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    def put(self, id, request):
        producto = self.get_object(id)
        serializer = ProductoSerializer(producto, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, id, request):
        producto = self.get_object(id)
        producto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)"""


class Producto_Detalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetalle(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Carrito(generics.CreateAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
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
            "productos": reverse("productos-list", request=request, format=format),
        }
    )


@api_view(["GET", "POST"])
def note(request):
    if request.method == "GET":
        note = Notes.objects.all()
        serializer = NoteSerializer(note, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def note_detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
