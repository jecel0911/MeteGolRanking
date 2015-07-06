# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jugadores', '0001_initial'),
        ('Campeonatos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pago', models.BooleanField(default=False)),
                ('fecha_pago', models.DateField()),
                ('campeonato', models.ForeignKey(to='Campeonatos.Campeonato')),
                ('jugador', models.ForeignKey(to='Jugadores.Jugador')),
            ],
            options={
                'verbose_name': 'Incripcione',
                'verbose_name_plural': 'Incripciones',
            },
        ),
    ]
