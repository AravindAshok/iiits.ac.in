# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-24 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0042_auto_20160624_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='news',
            field=models.TextField(default=''),
        ),
    ]