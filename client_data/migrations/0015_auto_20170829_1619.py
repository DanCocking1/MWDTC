# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_data', '0014_auto_20170829_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogstudent',
            name='classId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogstudent', to='client_data.DogClass'),
        ),
        migrations.AlterField(
            model_name='dogstudent',
            name='dogId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_data.Dog'),
        ),
    ]
