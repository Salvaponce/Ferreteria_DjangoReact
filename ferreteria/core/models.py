from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils import timezone


class Product(models.Model):
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=60, blank=False, default="")
    image = models.ImageField(blank=True, null=True, upload_to="products")
    stock = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, default="Otras")
    price = models.FloatField()

    class Meta:
        ordering = ["created"]


class Cart(models.Model):
    owner = models.ForeignKey(
        "auth.User", related_name="cart", on_delete=models.CASCADE, blank=True
    )
    products = models.ManyToManyField(Product, through="CartItem")


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("El nombre de usuario es obligatorio.")
        if not email:
            raise ValueError("La dirección de correo electrónico es obligatoria.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Especifica nombres de campos reversos personalizados
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        related_name="customuser_set",
        related_query_name="user",
    )
    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        related_name="customuser_set",
        related_query_name="user",
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
