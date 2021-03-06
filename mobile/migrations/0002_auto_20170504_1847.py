# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Rather Not Say')], default=0, max_length=1)),
                ('dob', models.DateField(blank=True, max_length=50, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=10, null=True)),
                ('country_code', models.CharField(blank=True, max_length=5, null=True)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('bio', models.CharField(blank=True, max_length=100, null=True)),
                ('join_date', models.DateTimeField(blank=True, max_length=50, null=True)),
                ('total_views', models.IntegerField(blank=True, default=0, null=True)),
                ('profile_pic', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('is_active', models.CharField(choices=[(0, 'InActive'), (1, 'Active')], default=1, max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
