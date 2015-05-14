# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_del_campeonato', models.CharField(max_length=25)),
                ('fecha_de_inicio', models.DateField()),
                ('fecha_de_fin', models.DateField(blank=True, null=True)),
                ('costo_de_la_inscripcion', models.DecimalField(max_digits=18, decimal_places=2)),
                ('descripcion', models.CharField(max_length=500)),
                ('reglas', models.TextField()),
            ],
            options={
                'verbose_name': 'Campeonato',
                'verbose_name_plural': 'Campeonatos',
            },
        ),
    ]
