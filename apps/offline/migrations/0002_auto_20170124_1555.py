# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-24 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issue',
            field=models.FileField(max_length=500, upload_to='images/offline', verbose_name='pdf'),
        ),
    ]