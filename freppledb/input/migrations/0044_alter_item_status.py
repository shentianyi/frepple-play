# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-25 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0043_item_status_change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(blank=True, choices=[('S0', 'S0'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('A0', 'A0'), ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3')], max_length=20, null=True, verbose_name='status'),
        ),
    ]
