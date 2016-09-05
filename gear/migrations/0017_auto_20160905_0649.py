# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0016_auto_20160903_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='gear.Item'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='gear.Item'),
        ),
    ]
