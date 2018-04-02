from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from producto.models import Suplidor, Producto


class SuplidorForm(forms.ModelForm):
    class Meta:
        model = Suplidor
        exclude = ('slug',)


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ('slug', 'fecha_ingreso')

    precio_unitario = forms.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(10000)]
    )
