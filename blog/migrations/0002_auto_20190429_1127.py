# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-29 11:27
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
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 11, 27, 17, 934442, tzinfo=utc)),
        ),
    ]
