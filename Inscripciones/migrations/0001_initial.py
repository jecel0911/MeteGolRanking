# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Campeonatos', '0002_auto_20150513_2104'),
        ('Jugadores', '0002_remove_jugador_puntos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pago', models.BooleanField(default=False)),
                ('campeonato', models.ForeignKey(to='Campeonatos.Campeonato')),
                ('jugador', models.ForeignKey(to='Jugadores.Jugador')),
            ],
            options={
                'verbose_name': 'Incripcione',
                'verbose_name_plural': 'Incripciones',
            },
        ),
    ]
