# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drops', '0009_remove_chapter_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='chapter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapter', to='drops.Chapter'),
        ),
    ]
