# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-25 16:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0041_create_itembom'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemRopQty',
            fields=[
                ('source', models.CharField(blank=True, db_index=True, max_length=300, null=True, verbose_name='source')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='last modified')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='updated_at')),
                ('id', models.AutoField(help_text='Unique identifier', primary_key=True, serialize=False, verbose_name='id')),
                ('qty', models.DecimalField(decimal_places=8, max_digits=20, verbose_name='rop qty')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemropqty_item', to='input.Item', verbose_name='item')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemropqty_location', to='input.Location', verbose_name='location')),
            ],
            options={
                'verbose_name': 'item rop qty',
                'verbose_name_plural': 'item rop qtys',
                'db_table': 'item_rop_qty',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemSafetyStock',
            fields=[
                ('source', models.CharField(blank=True, db_index=True, max_length=300, null=True, verbose_name='source')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='last modified')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='updated_at')),
                ('id', models.AutoField(help_text='Unique identifier', primary_key=True, serialize=False, verbose_name='id')),
                ('qty', models.DecimalField(decimal_places=8, max_digits=20, verbose_name='safety stock qty')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemsafetystock_item', to='input.Item', verbose_name='item')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemsafetystock_location', to='input.Location', verbose_name='location')),
            ],
            options={
                'verbose_name': 'item safety stock',
                'verbose_name_plural': 'item safety stocks',
                'db_table': 'item_safety_stock',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='itembom',
            name='qty',
            field=models.DecimalField(decimal_places=8, max_digits=20, verbose_name='qty'),
        ),
    ]
