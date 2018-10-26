# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-25 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operation',
            options={'ordering': ['id'], 'verbose_name': 'operation', 'verbose_name_plural': 'operations'},
        ),
        migrations.AlterField(
            model_name='operation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='operationmaterial',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operationmaterials_item', to='input.Item', verbose_name='item'),
        ),
        migrations.AlterField(
            model_name='operationmaterial',
            name='operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operationmaterials_operation', to='input.Operation', verbose_name='operation'),
        ),
        migrations.AlterField(
            model_name='operationplan',
            name='operation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operationplan_operation', to='input.Operation', verbose_name='operation'),
        ),
        migrations.AlterField(
            model_name='resourceskill',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resourceskill_resource', to='input.Resource', verbose_name='resource'),
        ),
        migrations.AlterField(
            model_name='resourceskill',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resourcesskill_skill', to='input.Skill', verbose_name='skill'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=300, verbose_name='name'),
        ),
    ]
