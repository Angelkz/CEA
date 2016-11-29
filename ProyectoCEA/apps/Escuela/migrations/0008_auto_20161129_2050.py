# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Escuela', '0007_auto_20161129_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materia',
            old_name='Serie',
            new_name='Clave',
        ),
    ]
