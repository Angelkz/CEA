# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Escuela', '0002_auto_20160512_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='Paquete',
            field=models.TextField(max_length=200),
        ),
    ]
