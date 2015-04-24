# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0004_auto_20150417_0306'),
        ('Tournement', '0005_auto_20150424_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=50)),
                ('points', models.DecimalField(max_digits=18, decimal_places=0)),
                ('games_played', models.DecimalField(max_digits=18, decimal_places=0)),
                ('wins', models.DecimalField(max_digits=18, decimal_places=0)),
                ('draws', models.DecimalField(max_digits=18, decimal_places=0)),
                ('looses', models.DecimalField(max_digits=18, decimal_places=0)),
                ('goals_for', models.DecimalField(max_digits=18, decimal_places=0)),
                ('goals_against', models.DecimalField(max_digits=18, decimal_places=0)),
                ('goals_difference', models.DecimalField(max_digits=18, decimal_places=0)),
                ('sets_win', models.DecimalField(max_digits=18, decimal_places=0)),
                ('sets_looses', models.DecimalField(max_digits=18, decimal_places=0)),
                ('player', models.ForeignKey(to='Player.Player')),
                ('tournement', models.ForeignKey(to='Tournement.Tournement')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
    ]
