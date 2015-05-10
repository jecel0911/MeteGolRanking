# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConceptosIngEgr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('codigo', models.CharField(max_length=5)),
                ('descripcion', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Concepto Ingresos/Egresos',
                'verbose_name_plural': 'Conceptos Ingresos/Egresos',
            },
        ),
        migrations.CreateModel(
            name='IngresosEgresos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha', models.DateTimeField()),
                ('monto', models.DecimalField(decimal_places=0, max_digits=18)),
                ('descripcion', models.CharField(max_length=50)),
                ('concepto', models.ForeignKey(to='IngresosEgresos.ConceptosIngEgr')),
            ],
            options={
                'verbose_name': 'Ingreso y Egreso',
                'verbose_name_plural': 'Ingresos y Egresos',
            },
        ),
    ]
