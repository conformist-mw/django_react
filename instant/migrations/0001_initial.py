# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(default=0)),
                ('birth', models.DateField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('ipv4', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('street', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
