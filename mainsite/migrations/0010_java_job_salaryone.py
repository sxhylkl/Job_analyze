# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-30 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0009_auto_20171228_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='java_job',
            name='salaryOne',
            field=models.IntegerField(max_length=16, null=True),
        ),
    ]
