# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0003_auto_20150416_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='idNumber',
            new_name='id_number',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='lastNam',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='shortName',
            new_name='player_name',
        ),
    ]
