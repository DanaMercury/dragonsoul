# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drops', '0003_auto_20160908_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='cost',
        ),
        migrations.AddField(
            model_name='chapter',
            name='cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]