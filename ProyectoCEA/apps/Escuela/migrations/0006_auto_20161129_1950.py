# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Escuela', '0005_auto_20161129_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='Autorizado',
            field=models.CharField(default=b'No', max_length=48),
        ),
    ]
