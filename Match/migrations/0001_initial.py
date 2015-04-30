# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0004_auto_20150417_0306'),
        ('Group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('set_1_player_1', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_1_player_2', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_2_player_1', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_2_player_2', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_3_player_1', models.DecimalField(max_digits=18, decimal_places=0)),
                ('set_3_player_2', models.DecimalField(max_digits=18, decimal_places=0)),
                ('group', models.ForeignKey(to='Group.Group')),
                ('player_one', models.ForeignKey(related_name='player_one', to='Player.Player')),
                ('player_two', models.ForeignKey(related_name='player_two', to='Player.Player')),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
            },
        ),
    ]
