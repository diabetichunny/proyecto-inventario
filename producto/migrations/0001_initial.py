# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(choices=[('Embutidos', 'Embutidos'), ('Frutas', 'Frutas'), ('Hortalizas', 'Hortalizas'), ('Enlatados', 'Enlatados'), ('Golosinas', 'Golosinas'), ('Cereales', 'Cereales')], max_length=10)),
                ('precio_unitario', models.FloatField()),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Suplidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('ubicacion', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='suplidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='producto.Suplidor'),
        ),
    ]