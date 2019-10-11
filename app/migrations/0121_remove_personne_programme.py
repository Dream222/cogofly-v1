# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0120_auto_20160414_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personne',
            name='programme',
        ),
    ]
