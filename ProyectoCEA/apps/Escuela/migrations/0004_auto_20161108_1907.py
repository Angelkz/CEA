# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Escuela', '0003_auto_20160609_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='Autorizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='NumeroEmpleado',
            field=models.CharField(default=123456789, max_length=48),
            preserve_default=False,
        ),
    ]
