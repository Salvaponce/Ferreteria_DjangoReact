from core import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.front, name="front"),
    path("products/", views.Product_List.as_view()),
    path("products/<int:pk>/", views.Product_Detalle.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    path("login/", views.LoginView.as_view()),
    path("signup/", views.RagistationView.as_view()),
    path("logout/", views.user_logout, name="user_logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
