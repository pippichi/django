# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-04-15 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0003_grade_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=16)),
                ('c_cost', models.IntegerField(default=10)),
            ],
        ),
    ]
