# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0140_auto_20160601_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personne',
            name='reactivate_code',
        ),
    ]
