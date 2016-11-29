# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Escuela', '0004_auto_20161108_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='Paquete',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
    ]
