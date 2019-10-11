# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20160127_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnetravel',
            name='ignore_end_dd',
        ),
        migrations.RemoveField(
            model_name='personnetravel',
            name='ignore_end_mm',
        ),
        migrations.RemoveField(
            model_name='personnetravel',
            name='ignore_start_dd',
        ),
        migrations.RemoveField(
            model_name='personnetravel',
            name='ignore_start_mm',
        ),
    ]
