# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Horario', '0003_salon_capacidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horariocarrera',
            old_name='Clave',
            new_name='Serie',
        ),
    ]
