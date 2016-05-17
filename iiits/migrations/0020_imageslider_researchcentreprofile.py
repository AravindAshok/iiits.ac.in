# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-23 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0019_auto_20160404_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='/static/iiits/images/imageslider')),
                ('order_no', models.PositiveIntegerField(default=0)),
                ('caption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ResearchCentreProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('people', models.TextField()),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iiits.ResearchCentre')),
            ],
        ),
    ]
