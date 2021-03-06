# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.IntegerField(choices=[(1, 'white'), (2, 'green'), (3, 'blue'), (4, 'purple'), (5, 'orange')], default=1)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('hero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='heroes.Hero')),
            ],
        ),
    ]
