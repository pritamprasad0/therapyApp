# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folderid', models.IntegerField()),
                ('foldername', models.CharField(max_length=20)),
                ('parentid', models.IntegerField()),
            ],
        ),
    ]
