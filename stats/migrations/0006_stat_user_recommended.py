# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-20 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_auto_20161118_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat_user',
            name='recommended',
            field=models.BooleanField(default=False),
        ),
    ]