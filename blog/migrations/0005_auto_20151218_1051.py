# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 07:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151218_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 7, 51, 35, 988833, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
