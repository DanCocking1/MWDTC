# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_data', '0024_auto_20170830_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogdayres',
            name='dogDayResCancelled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dogstudent',
            name='cancelledEnrollment',
            field=models.BooleanField(default=False),
        ),
    ]