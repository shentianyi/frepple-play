# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-21 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0013_alter_item_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemLocation',
            fields=[
                ('source', models.CharField(blank=True, db_index=True, max_length=300, null=True, verbose_name='source')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='last modified')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='updated_at')),
                ('id', models.AutoField(help_text='Unique identifier', primary_key=True, serialize=False, verbose_name='id')),
                ('type', models.CharField(choices=[('FG', 'FG'), ('WIP', 'WIP'), ('RM', 'RM')], max_length=20, verbose_name='type')),
                ('status', models.CharField(blank=True, choices=[('S0', 'S0'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4')], max_length=20, null=True, verbose_name='status')),
                ('plan_strategy', models.CharField(blank=True, choices=[('MTS', 'MTS'), ('MTO', 'MTO'), ('ETO', 'ETO')], max_length=20, null=True, verbose_name='plan strategy')),
                ('lock_type', models.CharField(blank=True, choices=[('locked', 'locked'), ('unlocked', 'unlocked')], default='unlocked', max_length=20, null=True, verbose_name='lock type')),
                ('lock_expire_at', models.DateField(blank=True, null=True, verbose_name='lock expire at')),
                ('inventory_qty', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True, verbose_name='inventory qty')),
                ('available_inventory', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True, verbose_name='available inventory')),
                ('inventory_cost', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True, verbose_name='inventory cost')),
                ('price_abc', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=20, null=True, verbose_name='price abc')),
                ('qty_abc', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=20, null=True, verbose_name='qty abc')),
                ('cost', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True, verbose_name='cost')),
                ('gross_weight', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True, verbose_name='gross weight')),
                ('net_weight', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True, verbose_name='net weight')),
                ('physical_unit', models.CharField(blank=True, max_length=20, null=True, verbose_name='physical unit')),
                ('project_nr', models.CharField(blank=True, db_index=True, max_length=300, null=True, verbose_name='project nr')),
                ('moq', models.DecimalField(decimal_places=8, max_digits=20, verbose_name='MOQ')),
                ('order_unit_qty', models.DecimalField(decimal_places=8, default=0, max_digits=20, verbose_name='order unit qty')),
                ('order_max_qty', models.DecimalField(decimal_places=8, default=0, max_digits=20, verbose_name='order max qty')),
                ('product_time', models.DecimalField(blank=True, decimal_places=8, default=0, max_digits=20, null=True, verbose_name='product time')),
                ('load_time', models.DecimalField(blank=True, decimal_places=8, default=0, max_digits=20, null=True, verbose_name='load time')),
                ('transit_time', models.DecimalField(blank=True, decimal_places=8, default=0, max_digits=20, null=True, verbose_name='transit time')),
                ('receive_time', models.DecimalField(blank=True, decimal_places=8, default=0, max_digits=20, null=True, verbose_name='receive time')),
                ('mpq', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True, verbose_name='mpq')),
                ('earliest_order_date', models.DateField(blank=True, null=True, verbose_name='earliest order date')),
                ('plan_supplier_date', models.DateField(blank=True, null=True, verbose_name='plan supplier date')),
                ('plan_load_date', models.DateField(blank=True, null=True, verbose_name='plan load date')),
                ('plan_receive_date', models.DateField(blank=True, null=True, verbose_name='plan receive date')),
                ('outer_package_num', models.IntegerField(blank=True, null=True, verbose_name='outer package num')),
                ('pallet_num', models.IntegerField(blank=True, null=True, verbose_name='pallet num')),
                ('outer_package_gross_weight', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True, verbose_name='outer package gross weight')),
                ('pallet_gross_weight', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True, verbose_name='pallet gross weight')),
                ('outer_package_volume', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True, verbose_name='outer package volume')),
                ('pallet_volume', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True, verbose_name='pallet volume')),
                ('plan_list_date', models.DateField(blank=True, db_index=True, null=True, verbose_name='plan list date')),
                ('plan_delist_date', models.DateField(blank=True, db_index=True, null=True, verbose_name='plan delist date')),
                ('category', models.CharField(blank=True, db_index=True, max_length=300, null=True, verbose_name='category')),
                ('subcategory', models.CharField(blank=True, db_index=True, max_length=300, null=True, verbose_name='subcategory')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='description')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemlocation_item', to='input.Item', verbose_name='sale item')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemlocation_location', to='input.Location', verbose_name='location')),
            ],
            options={
                'verbose_name': 'item location',
                'verbose_name_plural': 'item locations',
                'db_table': 'itemlocation',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='itemcustomer',
            options={'ordering': ['id'], 'verbose_name': 'item customer', 'verbose_name_plural': 'item customers'},
        ),
    ]