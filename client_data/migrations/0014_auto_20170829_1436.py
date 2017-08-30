# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_data', '0013_remove_dayrunreservation_available_runs'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayrunreservation',
            name='available_runs',
            field=models.PositiveSmallIntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='bathDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(),
        ),
    ]
