# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tournement', '0004_auto_20150417_0306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournement',
            old_name='tournement_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='tournement',
            name='begin_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 18, 11, 11, 820500, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournement',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 18, 11, 17, 808843, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournement',
            name='rules',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tournement',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
