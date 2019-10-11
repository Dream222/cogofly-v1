# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20151229_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='type_tag',
            field=models.CharField(default='0', max_length=1, choices=[('1', 'Job'), ('0', 'Enterprise'), ('3', 'Google maps'), ('2', 'Language'), ('5', 'Diploma'), ('4', 'Driving licences'), ('7', 'Hobby'), ('6', 'Point of interest')]),
        ),
        migrations.AlterField(
            model_name='tagwithvalue',
            name='type_tag',
            field=models.CharField(default='0', max_length=1, choices=[('1', 'Job'), ('0', 'Enterprise'), ('3', 'Google maps'), ('2', 'Language'), ('5', 'Diploma'), ('4', 'Driving licences'), ('7', 'Hobby'), ('6', 'Point of interest')]),
        ),
    ]
