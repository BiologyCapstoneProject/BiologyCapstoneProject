# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-26 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20170324_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateField(),
        ),
    ]
