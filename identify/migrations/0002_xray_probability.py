# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-20 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xray',
            name='probability',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
