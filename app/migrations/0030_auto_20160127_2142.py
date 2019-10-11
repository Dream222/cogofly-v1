# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20160127_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnetravel',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='personnetravel',
            name='date_start',
        ),
    ]
