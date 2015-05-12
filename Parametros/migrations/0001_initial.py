# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('jugadores_por_division', models.DecimalField(max_digits=18, decimal_places=0)),
                ('puntos_bono_primer_lugar_torneo', models.DecimalField(max_digits=18, decimal_places=0)),
                ('puntos_bono_segundo_lugar_torneo', models.DecimalField(max_digits=18, decimal_places=0)),
                ('puntos_bono_tercer_lugar_torneo', models.DecimalField(max_digits=18, decimal_places=0)),
                ('puntos_bono_cuarto_lugar_torneo', models.DecimalField(max_digits=18, decimal_places=0)),
                ('puntos_ganados_cuando_el_ganador_tiene_mas_puntos', models.DecimalField(max_digits=18, decimal_places=0)),
                ('puntos_ganados_cuando_el_ganador_tiene_menos_puntos', models.DecimalField(max_digits=18, decimal_places=0)),
                ('puntos_perdidos_cuando_el_perdedor_tiene_mas_puntos', models.DecimalField(max_digits=18, decimal_places=0)),
                ('puntos_perdidos_cuando_el_perdedor_tiene_menos_puntos', models.DecimalField(max_digits=18, decimal_places=0)),
            ],
            options={
                'verbose_name_plural': 'Parametros',
                'verbose_name': 'Parametros',
            },
        ),
    ]
