# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_data', '0015_auto_20170829_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes1',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes10',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes11',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes12',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes13',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes14',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes15',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes16',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes17',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes18',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes19',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes2',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes20',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes21',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes22',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes23',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes24',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes25',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes26',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes27',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes28',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes29',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes3',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes30',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes4',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes5',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes6',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes7',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes8',
        ),
        migrations.RemoveField(
            model_name='dayrunreservation',
            name='RunRes9',
        ),
        migrations.AddField(
            model_name='dayrunreservation',
            name='RunRes',
            field=models.ManyToManyField(to='client_data.Reservation'),
        ),
    ]
