# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 18:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_data', '0022_auto_20170830_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes',
        ),
    ]
