# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-24 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MWDTCClient',
            new_name='Client',
        ),
    ]
