# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app.models.date_partial_field


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20160125_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnetravel',
            name='new_end',
            field=app.models.date_partial_field.DatePartialField(default=None, null=True, verbose_name='End (m/d/Y)', blank=True),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='new_start',
            field=app.models.date_partial_field.DatePartialField(default=None, null=True, verbose_name='Start (m/d/Y)', blank=True),
        ),
        migrations.AlterField(
            model_name='personnetravel',
            name='date_start',
            field=models.DateTimeField(default=None, null=True, verbose_name='Start (m/d/Y)', blank=True),
        ),
    ]
