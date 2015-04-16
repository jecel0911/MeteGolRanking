# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournement', '0002_tournement_name2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournement',
            name='name2',
        ),
    ]
