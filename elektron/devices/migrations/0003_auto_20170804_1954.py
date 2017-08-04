# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_remove_device_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='measure',
        ),
        migrations.AddField(
            model_name='device',
            name='device_mac',
            field=models.CharField(blank=True, default='0', max_length=100),
        ),
    ]