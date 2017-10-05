# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_data', '0032_remove_dogstudent_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogclass',
            name='enrollmentSlots',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dogclass',
            name='startTime',
            field=models.CharField(default='6 pm', max_length=12),
        ),
    ]
