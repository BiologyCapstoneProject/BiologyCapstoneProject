# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 21:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20170406_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 21, 1, 3, 928974)),
        ),
    ]
