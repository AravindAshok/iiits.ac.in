# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-23 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0008_admissionsfinancialassistance_admissionspolicy'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionsfeestructure',
            name='academic_year',
            field=models.CharField(default='2016-2017', max_length=200),
        ),
    ]
