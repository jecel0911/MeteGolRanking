# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Campeonatos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('division', models.PositiveSmallIntegerField()),
                ('campeonato', models.ForeignKey(to='Campeonatos.Campeonato')),
            ],
            options={
                'verbose_name': 'Torneo',
                'verbose_name_plural': 'Torneos',
            },
        ),
    ]
