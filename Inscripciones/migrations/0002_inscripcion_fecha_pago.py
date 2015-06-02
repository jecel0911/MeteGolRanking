# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Inscripciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcion',
            name='fecha_pago',
            field=models.DateField(default=datetime.datetime(2015, 6, 2, 3, 3, 13, 597716, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
