# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parameter', '0002_auto_20150417_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='bonus_points_1_place',
            field=models.DecimalField(default=0, max_digits=18, decimal_places=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='bonus_points_2_place',
            field=models.DecimalField(default=0, max_digits=18, decimal_places=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='bonus_points_3_place',
            field=models.DecimalField(default=0, max_digits=18, decimal_places=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='bonus_points_4_place',
            field=models.DecimalField(default=0, max_digits=18, decimal_places=0),
            preserve_default=False,
        ),
    ]
