# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_auto_20170504_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InterestsContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('image', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='interests',
            name='interest_content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.InterestsContent'),
        ),
        migrations.AddField(
            model_name='interests',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.users'),
        ),
    ]
