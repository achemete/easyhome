# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-14 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appApi', '0010_auto_20180114_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='attractions',
            name='image2',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attractions',
            name='image3',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image2',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image3',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
