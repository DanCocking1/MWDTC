# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_data', '0028_dogstudent_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email_address',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]