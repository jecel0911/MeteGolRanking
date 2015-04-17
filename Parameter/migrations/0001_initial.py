# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('players_by_division', models.DecimalField(max_digits=18, decimal_places=0)),
                ('points_earned_when_winner_is_higher', models.DecimalField(max_digits=18, decimal_places=0)),
                ('points_earned_when_winner_is_lower', models.DecimalField(max_digits=18, decimal_places=0)),
                ('points_earned_when_loser_is_higher', models.DecimalField(max_digits=18, decimal_places=0)),
                ('points_earned_when_loser_is_lower', models.DecimalField(max_digits=18, decimal_places=0)),
            ],
        ),
    ]
