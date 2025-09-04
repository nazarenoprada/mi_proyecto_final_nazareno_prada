from django.db import models

class Producto(models.Model):
    """
    Modelo para representar un producto en la tienda.
    """
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        """
        Retorna una representación en cadena del producto.
        """
        return self.nombre
