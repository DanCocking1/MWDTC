# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_data', '0035_auto_20171011_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='medication',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
    ]
