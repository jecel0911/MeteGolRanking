# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0005_auto_20150424_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='nick_name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
