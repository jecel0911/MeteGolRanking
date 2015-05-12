# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=10)),
                ('apellidos', models.CharField(max_length=50)),
                ('apodo', models.CharField(max_length=25, blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('puntos', models.DecimalField(max_digits=18, decimal_places=0)),
            ],
            options={
                'verbose_name_plural': 'Jugadores',
                'verbose_name': 'Jugador',
            },
        ),
    ]
