# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-14 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drops', '0015_auto_20161114_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stage',
            old_name='level',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='level',
        ),
        migrations.AddField(
            model_name='chapter',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]