# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Escuela', '0006_auto_20161129_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='NumeroEmpleado',
            new_name='NumeroDocente',
        ),
    ]
