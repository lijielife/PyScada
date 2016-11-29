# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0008_auto_20161124_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exporttask',
            name='fineshed',
        ),
        migrations.RemoveField(
            model_name='exporttask',
            name='start',
        ),
        migrations.RemoveField(
            model_name='exporttask',
            name='time_max',
        ),
        migrations.RemoveField(
            model_name='exporttask',
            name='time_min',
        ),
        migrations.AlterField(
            model_name='scheduledexporttask',
            name='day_time',
            field=models.PositiveSmallIntegerField(choices=[(0, b'0:00'), (1, b'1:00'), (2, b'2:00'), (3, b'3:00'), (4, b'4:00'), (5, b'5:00'), (6, b'6:00'), (7, b'7:00'), (8, b'8:00'), (9, b'9:00'), (10, b'10:00'), (11, b'11:00'), (12, b'12:00'), (13, b'13:00'), (14, b'14:00'), (15, b'15:00'), (16, b'16:00'), (17, b'17:00'), (18, b'18:00'), (19, b'19:00'), (20, b'20:00'), (21, b'21:00'), (22, b'22:00'), (23, b'23:00')], default=0, help_text=b'day time wenn the job will be started in UTC'),
        ),
    ]
