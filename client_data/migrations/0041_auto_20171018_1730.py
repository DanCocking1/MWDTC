# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-18 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_data', '0040_privatedogclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatedogclass',
            name='classId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classtaken', to='client_data.DogClass'),
        ),
    ]
