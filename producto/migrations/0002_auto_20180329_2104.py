# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suplidor',
            name='ubicacion',
            field=models.TextField(),
        ),
    ]
