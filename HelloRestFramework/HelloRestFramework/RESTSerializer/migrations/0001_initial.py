# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-04-19 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=32)),
                ('p_age', models.IntegerField(default=1)),
                ('p_sex', models.BooleanField(default=False)),
            ],
        ),
    ]
