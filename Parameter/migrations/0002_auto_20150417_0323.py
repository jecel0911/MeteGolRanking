# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parameter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parameter',
            options={'verbose_name': 'Parameter', 'verbose_name_plural': 'Parameters'},
        ),
    ]
