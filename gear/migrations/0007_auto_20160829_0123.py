# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0006_auto_20160829_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_color',
            field=models.IntegerField(choices=[(1, 'white'), (2, 'green'), (3, 'blue'), (4, 'purple'), (5, 'orange')]),
        ),
    ]
