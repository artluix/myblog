# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 06:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151218_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 6, 47, 27, 393573, tzinfo=utc)),
        ),
    ]
