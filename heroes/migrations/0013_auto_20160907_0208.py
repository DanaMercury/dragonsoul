# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 02:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0012_auto_20160907_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='hero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quests', to='heroes.Hero'),
        ),
    ]
