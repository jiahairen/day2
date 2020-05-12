# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-05-11 15:15
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
                ('p_name', models.CharField(max_length=16, unique=True)),
                ('p_age', models.IntegerField(db_column='age', default=18)),
                ('p_sex', models.BooleanField(db_column='sex', default=True)),
            ],
        ),
    ]