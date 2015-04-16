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
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=250)),
                ('inscriptionCost', models.DecimalField(max_digits=18, decimal_places=2)),
                ('minRanking', models.DecimalField(max_digits=18, decimal_places=0)),
                ('maxRanking', models.DecimalField(max_digits=18, decimal_places=0)),
            ],
            options={
                'verbose_name': 'Tournement',
                'verbose_name_plural': 'Tournements',
            },
        ),
    ]
