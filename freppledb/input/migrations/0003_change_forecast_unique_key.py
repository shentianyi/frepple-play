# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-01 18:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0002_add_parsed_date_to_forecast'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='forecast',
            unique_together=set([('item', 'location', 'customer', 'year', 'date_type', 'date_number', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='forecastyear',
            unique_together=set([('item', 'location', 'customer', 'year', 'date_type', 'date_number')]),
        ),
    ]
