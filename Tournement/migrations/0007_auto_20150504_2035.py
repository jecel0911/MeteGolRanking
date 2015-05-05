# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournement', '0006_auto_20150504_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournement',
            name='finish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
