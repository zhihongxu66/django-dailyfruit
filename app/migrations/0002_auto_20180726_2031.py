# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-26 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_ticket',
            name='out_time',
            field=models.DateTimeField(default=0),
        ),
    ]
