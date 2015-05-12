# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Grupos', '0001_initial'),
        ('Jugadores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('fecha', models.DateField()),
                ('set_1_jugador_1', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_1_jugador_2', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_2_jugador_1', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_2_jugador_2', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_3_jugador_1', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_3_jugador_2', models.DecimalField(max_digits=18, decimal_places=0)),
                ('grupo', models.ForeignKey(to='Grupos.Grupo')),
                ('jugador_dos', models.ForeignKey(related_name='player_two', to='Jugadores.Jugador')),
                ('jugador_uno', models.ForeignKey(related_name='player_one', to='Jugadores.Jugador')),
            ],
            options={
                'verbose_name_plural': 'Partidos',
                'verbose_name': 'Partido',
            },
        ),
    ]
