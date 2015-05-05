# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournement', '0005_auto_20150424_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournement',
            name='finish_date',
            field=models.DateTimeField(null=True),
        ),
    ]
