# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0142_auto_20160601_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='est_active',
            field=models.BooleanField(default=True),
        ),
    ]
