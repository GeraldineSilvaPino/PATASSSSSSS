from django.db import models
from django.contrib.auth.models import User  # Si estás utilizando el modelo User de Django

class Compra(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Compra de {self.user.username} - Total: ${self.total}"
    
class CompraItem(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='items')
    producto_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.producto_name} en {self.compra}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/')  # Asume que estás utilizando ImageField

    def __str__(self):
        return self.nombre