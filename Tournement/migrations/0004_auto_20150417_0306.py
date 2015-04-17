# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournement', '0003_remove_tournement_name2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournement',
            old_name='inscriptionCost',
            new_name='inscription_cost',
        ),
        migrations.RemoveField(
            model_name='tournement',
            name='maxRanking',
        ),
        migrations.RemoveField(
            model_name='tournement',
            name='minRanking',
        ),
        migrations.RemoveField(
            model_name='tournement',
            name='name',
        ),
        migrations.AddField(
            model_name='tournement',
            name='tournement_name',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
