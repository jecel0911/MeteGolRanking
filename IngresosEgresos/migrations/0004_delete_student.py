# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IngresosEgresos', '0003_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
