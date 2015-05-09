# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IngresosEgresos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresosegresos',
            name='fecha',
            field=models.DateField(),
        ),
    ]
