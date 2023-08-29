from core import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", views.front, name="front"),
    path("products/", views.Product_List.as_view()),
    path("products/<int:pk>/", views.Product_Detalle.as_view()),
    path("api-auth/", include("rest_framework.urls")),
]
