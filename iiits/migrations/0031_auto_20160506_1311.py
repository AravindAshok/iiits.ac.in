# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-06 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0030_remove_staff_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('notification', models.FileField(upload_to='iiits/static/files/careers/')),
                ('is_expired', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CareerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='publication',
            name='fileupload',
            field=models.FileField(upload_to='iiits/static/files/publications/'),
        ),
    ]
