# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_data', '0016_auto_20170829_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayrunreservation',
            name='RunRes',
            field=models.ManyToManyField(related_name='RunRes', to='client_data.Reservation'),
        ),
    ]
