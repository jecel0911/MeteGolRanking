# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournement',
            name='name2',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
