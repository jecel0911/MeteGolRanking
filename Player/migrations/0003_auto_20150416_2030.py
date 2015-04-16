# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0002_auto_20150413_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='idNumber',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='lastNam',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
