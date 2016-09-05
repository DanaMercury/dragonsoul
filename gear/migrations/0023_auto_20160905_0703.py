# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0022_auto_20160905_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='gear.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gear.Item'),
        ),
    ]
