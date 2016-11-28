# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Horario', '0002_auto_20160512_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='Capacidad',
            field=models.IntegerField(default=b'0'),
        ),
    ]
