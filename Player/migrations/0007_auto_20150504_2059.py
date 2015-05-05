# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0006_player_nick_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='nick_name',
            field=models.CharField(blank=True, null=True, max_length=25),
        ),
    ]
