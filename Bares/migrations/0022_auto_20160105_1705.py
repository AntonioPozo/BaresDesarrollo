# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bares', '0021_auto_20160105_1700'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Precios',
        ),
        migrations.AddField(
            model_name='bar',
            name='precio_cubata',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='bar',
            name='precio_refresco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='bar',
            name='precio_cerveza',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
