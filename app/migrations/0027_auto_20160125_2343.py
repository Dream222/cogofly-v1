# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20160125_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnetravel',
            name='date_end_dd',
        ),
        migrations.RemoveField(
            model_name='personnetravel',
            name='date_end_mm',
        ),
        migrations.RemoveField(
            model_name='personnetravel',
            name='date_end_yy',
        ),
        migrations.RemoveField(
            model_name='personnetravel',
            name='date_start_dd',
        ),
        migrations.RemoveField(
            model_name='personnetravel',
            name='date_start_mm',
        ),
        migrations.RemoveField(
            model_name='personnetravel',
            name='date_start_yy',
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='ignore_end_dd',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='ignore_end_mm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='ignore_start_dd',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='ignore_start_mm',
            field=models.BooleanField(default=False),
        ),
    ]
