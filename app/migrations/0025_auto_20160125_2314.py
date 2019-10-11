# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20160125_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnetravel',
            name='date_end',
            field=models.DateTimeField(default=None, null=True, verbose_name='End', blank=True),
        ),
        migrations.AlterField(
            model_name='personnetravel',
            name='date_start',
            field=models.DateTimeField(default=None, null=True, verbose_name='Start', blank=True),
        ),
    ]
