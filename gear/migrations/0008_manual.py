# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0007_auto_20160829_0123'),
    ]

    operations = [
        migrations.RenameField('item', 'item_name', 'name'),
        migrations.RenameField('item', 'item_color', 'color'),
    ]
