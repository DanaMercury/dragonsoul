# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0030_auto_20160907_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(height_field='height', null=True, upload_to='items', width_field='width'),
        ),
        migrations.AddField(
            model_name='item',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]