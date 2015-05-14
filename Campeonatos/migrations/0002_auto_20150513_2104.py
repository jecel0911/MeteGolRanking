# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Campeonatos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campeonato',
            old_name='costo_de_la_inscripcion',
            new_name='costo_inscripcion',
        ),
        migrations.RenameField(
            model_name='campeonato',
            old_name='fecha_de_fin',
            new_name='fecha_fin',
        ),
        migrations.RenameField(
            model_name='campeonato',
            old_name='fecha_de_inicio',
            new_name='fecha_inicio',
        ),
        migrations.RenameField(
            model_name='campeonato',
            old_name='nombre_del_campeonato',
            new_name='nombre',
        ),
    ]
