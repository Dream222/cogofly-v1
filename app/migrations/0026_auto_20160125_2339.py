# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20160125_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnetravel',
            name='date_end_dd',
            field=models.IntegerField(default=None, null=True, blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='date_end_mm',
            field=models.IntegerField(default=None, null=True, blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='date_end_yy',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='date_start_dd',
            field=models.IntegerField(default=None, null=True, blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='date_start_mm',
            field=models.IntegerField(default=None, null=True, blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='date_start_yy',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
    ]
