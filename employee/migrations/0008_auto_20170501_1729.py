# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20170419_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componentcategory',
            name='category_id',
        ),
        migrations.AlterField(
            model_name='componentcategory',
            name='category_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]
