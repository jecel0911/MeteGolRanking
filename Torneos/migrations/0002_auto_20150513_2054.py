# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Campeonatos', '0001_initial'),
        ('Torneos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='torneo',
            name='costo_de_la_inscripcion',
        ),
        migrations.RemoveField(
            model_name='torneo',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='torneo',
            name='fecha_de_fin',
        ),
        migrations.RemoveField(
            model_name='torneo',
            name='fecha_de_inicio',
        ),
        migrations.RemoveField(
            model_name='torneo',
            name='reglas',
        ),
        migrations.AddField(
            model_name='torneo',
            name='campeonato',
            field=models.ForeignKey(to='Campeonatos.Campeonato', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='torneo',
            name='division',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
