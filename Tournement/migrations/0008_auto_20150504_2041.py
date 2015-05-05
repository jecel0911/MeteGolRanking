# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournement', '0007_auto_20150504_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournement',
            name='rules',
            field=models.TextField(),
        ),
    ]
