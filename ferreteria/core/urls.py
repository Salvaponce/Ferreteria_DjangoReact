from core import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", views.front, name="front"),
    path("products", views.Producto_List.as_view()),
    path("products/<int:id>", views.Producto_Detalle.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    path("notes/", views.note, name="note"),
    path("notes/<int:pk>/", views.note_detail, name="detail"),
]
