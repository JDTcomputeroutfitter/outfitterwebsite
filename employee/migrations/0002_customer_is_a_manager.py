# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_a_manager',
            field=models.BooleanField(default=False),
        ),
    ]
