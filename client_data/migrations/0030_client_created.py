# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 19:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client_data', '0029_auto_20171001_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]