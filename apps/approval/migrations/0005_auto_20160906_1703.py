# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-06 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approval', '0004_auto_20160309_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipapproval',
            name='field_of_study',
            field=models.SmallIntegerField(choices=[(0, 'Gjest'), (1, 'Bachelor i Informatikk'), (10, 'Programvaresystemer'), (11, 'Databaser og søk'), (12, 'Algoritmer og datamaskiner'), (13, 'Spillteknologi'), (14, 'Kunstig intelligens'), (15, 'Helseinformatikk'), (16, 'Interaksjonsdesign, spill- og læringsteknologi'), (30, 'Annen mastergrad'), (80, 'PhD'), (90, 'International'), (100, 'Annet Onlinemedlem')], default=0, verbose_name='studieretning'),
        ),
    ]