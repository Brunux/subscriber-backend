# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-04 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocid', models.CharField(max_length=50, verbose_name='OCID')),
                ('planning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.Planning')),
            ],
        ),
    ]
