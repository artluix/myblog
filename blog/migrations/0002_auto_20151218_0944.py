# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 06:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 6, 44, 7, 864997, tzinfo=utc)),
        ),
    ]