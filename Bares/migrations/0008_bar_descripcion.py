# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bares', '0007_precios'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='descripcion',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]