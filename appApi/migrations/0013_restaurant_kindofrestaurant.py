# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-14 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appApi', '0012_auto_20180114_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='kindOfRestaurant',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]