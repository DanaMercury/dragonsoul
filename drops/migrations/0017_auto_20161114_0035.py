# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-14 00:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drops', '0016_auto_20161114_0018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ['number']},
        ),
    ]
