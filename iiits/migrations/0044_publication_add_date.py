# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-29 06:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0043_auto_20160624_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=datetime.datetime(2016, 6, 29, 6, 4, 17, 172231, tzinfo=utc)),
            preserve_default=False,
        ),
    ]