# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bares', '0006_auto_20151216_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refresco', models.IntegerField()),
                ('cerveza', models.IntegerField()),
                ('cubata', models.IntegerField()),
            ],
        ),
    ]
