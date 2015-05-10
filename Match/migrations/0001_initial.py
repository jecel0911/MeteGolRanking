# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0001_initial'),
        ('Player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('set_1_jugador_1', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_1_jugador_2', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_2_jugador_1', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_2_jugador_2', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_3_jugador_1', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_3_jugador_2', models.DecimalField(max_digits=18, decimal_places=0)),
                ('group', models.ForeignKey(to='Group.Group')),
                ('jugador_dos', models.ForeignKey(related_name='player_two', to='Player.Player')),
                ('jugador_uno', models.ForeignKey(related_name='player_one', to='Player.Player')),
            ],
            options={
                'verbose_name': 'Partido',
                'verbose_name_plural': 'Partidos',
            },
        ),
    ]
