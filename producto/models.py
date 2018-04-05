from django.core.urlresolvers import reverse
from django.db import models
from django.template import defaultfilters

# Create your models here.


class Suplidor(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    ubicacion = models.TextField()
    fecha_ingreso = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('supplier_list')

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre)
        super(Suplidor, self).save(*args, **kwargs)


class Producto(models.Model):
    tipos = (
        ('Embutidos', 'Embutidos'),
        ('Frutas', 'Frutas'),
        ('Hortalizas', 'Hortalizas'),
        ('Enlatados', 'Enlatados'),
        ('Golosinas', 'Golosinas'),
        ('Cereales', 'Cereales'),
        ('Bebidas', 'Bebidas'),
        ('Víveres', 'Víveres'),
        ('Higiene', 'Higiene')
    )

    # Model Fields
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=100)
    tipo = models.CharField(max_length=10, choices=tipos)
    suplidor = models.ForeignKey(Suplidor, related_name='productos')
    precio_unitario = models.FloatField()
    cantidad = models.PositiveSmallIntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre)
        super(Producto, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('supplier_list')
