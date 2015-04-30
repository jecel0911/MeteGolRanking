# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0005_auto_20150424_2057'),
        ('Group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            ],
            options={
                'verbose_name': 'Group Detail',
                'verbose_name_plural': 'Group Details',
            },
        ),
        migrations.RemoveField(
            model_name='group',
            name='draws',
        ),
        migrations.RemoveField(
            model_name='group',
            name='games_played',
        ),
        migrations.RemoveField(
            model_name='group',
            name='goals_against',
        ),
        migrations.RemoveField(
            model_name='group',
            name='goals_difference',
        ),
        migrations.RemoveField(
            model_name='group',
            name='goals_for',
        ),
        migrations.RemoveField(
            model_name='group',
            name='looses',
        ),
        migrations.RemoveField(
            model_name='group',
            name='player',
        ),
        migrations.RemoveField(
            model_name='group',
            name='points',
        ),
        migrations.RemoveField(
            model_name='group',
            name='sets_looses',
        ),
        migrations.RemoveField(
            model_name='group',
            name='sets_win',
        ),
        migrations.RemoveField(
            model_name='group',
            name='wins',
        ),
        migrations.AddField(
            model_name='groupdetail',
            name='group',
            field=models.ForeignKey(to='Group.Group'),
        ),
        migrations.AddField(
            model_name='groupdetail',
            name='player',
            field=models.ForeignKey(to='Player.Player'),
        ),
    ]
