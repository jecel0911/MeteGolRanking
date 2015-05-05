# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parameter', '0003_auto_20150424_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameter',
            old_name='points_earned_when_winner_is_higher',
            new_name='earned_points_when_winner_is_higher',
        ),
        migrations.RenameField(
            model_name='parameter',
            old_name='points_earned_when_winner_is_lower',
            new_name='earned_points_when_winner_is_lower',
        ),
        migrations.RenameField(
            model_name='parameter',
            old_name='points_earned_when_loser_is_higher',
            new_name='lost_points_when_loser_is_higher',
        ),
        migrations.RenameField(
            model_name='parameter',
            old_name='points_earned_when_loser_is_lower',
            new_name='lost_points_when_loser_is_lower',
        ),
    ]
