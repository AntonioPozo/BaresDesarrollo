# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bares', '0015_auto_20151221_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='logo',
            field=models.ImageField(default=b'building.jpg', upload_to=b'static'),
        ),
    ]