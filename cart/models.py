from django.db import models
from productos.models import Producto

class Carrito(models.Model):
    session_key = models.CharField(max_length=40, unique=True, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Carrito de {self.session_key}"

class ProductoCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='productos_en_carrito')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    agregado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('carrito', 'producto')

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    
    