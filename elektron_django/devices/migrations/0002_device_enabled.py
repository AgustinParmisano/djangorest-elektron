# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
    ]
