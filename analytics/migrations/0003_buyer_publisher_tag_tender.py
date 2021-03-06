# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-04 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oic', models.CharField(max_length=30)),
                ('language', models.CharField(max_length=30)),
                ('initiationType', models.CharField(max_length=30)),
                ('buyerId', models.CharField(max_length=10)),
                ('buyerName', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.URLField()),
                ('uid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cero', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('procurentMethodRationale', models.CharField(max_length=30)),
                ('procurentMethod', models.CharField(max_length=30)),
                ('tenderId', models.CharField(max_length=10)),
                ('hasEnquiries', models.BooleanField()),
                ('description', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('period', models.DateTimeField()),
                ('submissionMethod', models.CharField(max_length=10)),
                ('procuringEntityName', models.CharField(max_length=30)),
                ('procuringEntityId', models.CharField(max_length=30)),
                ('enquiryPeriodStartDate', models.DateTimeField()),
            ],
        ),
    ]
