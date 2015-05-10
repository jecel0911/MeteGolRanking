# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_del_torneo', models.CharField(max_length=25)),
                ('fecha_de_inicio', models.DateTimeField()),
                ('fecha_de_fin', models.DateTimeField(null=True, blank=True)),
                ('costo_de_la_inscripcion', models.DecimalField(max_digits=18, decimal_places=2)),
                ('descripcion', models.CharField(max_length=500)),
                ('reglas', models.TextField()),
            ],
            options={
                'verbose_name': 'Torneo',
                'verbose_name_plural': 'Torneos',
            },
        ),
    ]
