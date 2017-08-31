# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_data', '0019_auto_20170830_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogreservation',
            name='day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayres', to='client_data.DayRunReservation'),
        ),
        migrations.AlterField(
            model_name='dogreservation',
            name='reservation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='foundres', to='client_data.Reservation'),
        ),
    ]
