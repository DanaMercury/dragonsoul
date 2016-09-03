# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0012_item_equippable'),
        ('heroes', '0005_auto_20160903_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='rarity',
            name='gear3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gear3', to='gear.Item'),
        ),
        migrations.AddField(
            model_name='rarity',
            name='gear4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gear4', to='gear.Item'),
        ),
        migrations.AddField(
            model_name='rarity',
            name='gear5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gear5', to='gear.Item'),
        ),
        migrations.AddField(
            model_name='rarity',
            name='gear6',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gear6', to='gear.Item'),
        ),
    ]
