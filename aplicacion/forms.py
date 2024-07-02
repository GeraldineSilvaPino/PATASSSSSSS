from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'imagen']

class CrearCuentaForm(UserCreationForm):
    pass
