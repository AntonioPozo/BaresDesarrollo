# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bares', '0018_auto_20151222_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='tapa',
            name='megustas',
            field=models.IntegerField(default=0),
        ),
    ]
