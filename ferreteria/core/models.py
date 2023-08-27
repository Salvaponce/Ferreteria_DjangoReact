from django.db import models


class Producto(models.Model):
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=60, blank=False, default="")
    imagen = models.ImageField()
    stock = models.BooleanField(default=False)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50, default="Otras")

    class Meta:
        ordering = ["created"]


class Carrito(models.Model):
    owner = models.ForeignKey(
        "auth.User", related_name="productos", on_delete=models.CASCADE
    )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()


class Notes(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=120)

    def __str__(self):
        return self.title
