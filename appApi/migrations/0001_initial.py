# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100, blank=True)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.URLField()),
                ('visibility', models.BooleanField(default=True)),
                ('guests', models.IntegerField(default=1)),
                ('bedrooms', models.IntegerField(default=1)),
                ('beds', models.IntegerField(default=1)),
                ('bathroom', models.IntegerField(default=1)),
                ('extraInfo', models.TextField()),
                ('city', models.CharField(default=b'', max_length=100)),
                ('kindOfHouse', models.CharField(default=b'', max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('image', models.URLField()),
                ('city', models.CharField(default=b'', max_length=100)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField(default=b'')),
                ('accomodations', models.ForeignKey(to='appApi.Accomodations')),
                ('attractions', models.ForeignKey(to='appApi.Attractions')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('image', models.URLField()),
                ('city', models.CharField(default=b'', max_length=100)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('stars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wifi', models.BooleanField(default=True)),
                ('shower', models.BooleanField(default=True)),
                ('kitchen', models.BooleanField(default=True)),
                ('surveillanceCamera', models.BooleanField(default=True)),
                ('HeatingSystem', models.BooleanField(default=True)),
                ('Television', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(default=b'', max_length=100, blank=True)),
                ('surname', models.CharField(default=b'', max_length=100, blank=True)),
                ('email', models.EmailField(default=b'', max_length=254)),
                ('userId', models.CharField(default=b'', unique=True, max_length=100, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='deal',
            name='restaurant',
            field=models.ForeignKey(to='appApi.Restaurant'),
        ),
        migrations.AddField(
            model_name='accomodations',
            name='owner',
            field=models.ForeignKey(to='appApi.Users'),
        ),
        migrations.AddField(
            model_name='accomodations',
            name='reviews',
            field=models.ForeignKey(to='appApi.Reviews'),
        ),
        migrations.AddField(
            model_name='accomodations',
            name='services',
            field=models.ForeignKey(to='appApi.Services'),
        ),
    ]
