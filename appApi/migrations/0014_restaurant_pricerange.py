# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-14 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appApi', '0013_restaurant_kindofrestaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='priceRange',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
    ]
