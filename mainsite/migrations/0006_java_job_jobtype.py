# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-27 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20171226_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='java_job',
            name='jobType',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
