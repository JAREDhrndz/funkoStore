from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']  


# forms.py
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    # Puedes agregar más campos si deseas personalizar el formulario
    pass
