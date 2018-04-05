import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inventario.settings")
django.setup()

from faker import Faker
from producto.models import Suplidor, Producto
import random

fakegen = Faker('es_MX')


def populate_suppliers(N):
    suppliers = []

    for entry in range(N):
        while True:
            try:
                suppliers.append(Suplidor.objects.create(
                    nombre=fakegen.company(),
                    ubicacion=fakegen.address()
                ))
            except:
                continue
            break
    return suppliers


def populate_products(N=20):
    tipos = ['Embutidos', 'Frutas', 'Hortalizas',
             'Enlatados', 'Golosinas', 'Cereales',
             'Víveres', 'Higiene', 'Bebidas']

    suplidores = populate_suppliers(round(N / 4))

    for entry in range(N):
        while True:
            try:
                Producto.objects.create(
                    nombre=' '.join(fakegen.words(random.choice(range(1, 4)))),
                    descripcion=fakegen.text(20),
                    tipo=random.choice(tipos),
                    suplidor=random.choice(suplidores),
                    precio_unitario=fakegen.pyfloat(
                        left_digits=random.choice(range(1, 4)),
                        right_digits=random.choice(range(1, 4)),
                        positive=True
                    ),
                    cantidad=random.choice(range(1, 50))
                )
            except:
                continue
            break


if __name__ == '__main__':
    print("~~~~ Populating Proccess Starting! ~~~~")
    populate_products(100)
    print("~~~~ Populating Proccess Complete! ~~~~")
