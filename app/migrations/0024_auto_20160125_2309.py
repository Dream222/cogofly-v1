# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20160120_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnetravel',
            name='date_end',
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='is_past',
            field=models.BooleanField(default=False, verbose_name='This is a past travel'),
        ),
        migrations.AlterField(
            model_name='personnetravel',
            name='date_start',
            field=models.DateTimeField(default=None, null=True, verbose_name='End', blank=True),
        ),
    ]
