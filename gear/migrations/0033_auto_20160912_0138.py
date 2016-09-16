# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 01:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0032_auto_20160911_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='gear.Item'),
        ),
    ]
