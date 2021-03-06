# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jugadores', '0001_initial'),
        ('Torneos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleGrupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puntos', models.DecimalField(max_digits=18, decimal_places=0)),
                ('partidos_jugados', models.DecimalField(max_digits=18, decimal_places=0)),
                ('partidos_ganados', models.DecimalField(max_digits=18, decimal_places=0)),
                ('partidos_perdidos', models.DecimalField(max_digits=18, decimal_places=0)),
                ('goles_a_favor', models.DecimalField(max_digits=18, decimal_places=0)),
                ('goles_en_contra', models.DecimalField(max_digits=18, decimal_places=0)),
                ('goles_de_diferencia', models.DecimalField(max_digits=18, decimal_places=0)),
                ('sets_ganados', models.DecimalField(max_digits=18, decimal_places=0)),
                ('sets_perdidos', models.DecimalField(max_digits=18, decimal_places=0)),
            ],
            options={
                'verbose_name': 'Detalle del grupo',
                'verbose_name_plural': 'Detalles del grupo',
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50)),
                ('torneo', models.ForeignKey(to='Torneos.Torneo')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
            },
        ),
        migrations.AddField(
            model_name='detallegrupo',
            name='grupo',
            field=models.ForeignKey(to='Grupos.Grupo'),
        ),
        migrations.AddField(
            model_name='detallegrupo',
            name='jugador',
            field=models.ForeignKey(to='Jugadores.Jugador'),
        ),
    ]
