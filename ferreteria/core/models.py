from django.db import models


class Product(models.Model):
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=60, blank=False, default="")
    imagen = models.ImageField(blank=True, null=True)
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
