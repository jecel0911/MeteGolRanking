# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0004_auto_20150417_0306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='last_name',
            new_name='last_name_1',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='ranking',
            new_name='points',
        ),
        migrations.AddField(
            model_name='player',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='last_name_2',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]
