# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Torneos', '0002_auto_20150513_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='torneo',
            old_name='nombre_del_torneo',
            new_name='nombre',
        ),
    ]
