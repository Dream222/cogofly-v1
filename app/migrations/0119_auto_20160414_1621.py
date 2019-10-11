# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0118_auto_20160414_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnephoto',
            name='photo_type',
            field=models.IntegerField(default=0, choices=[(0, 'Profil'), (1, 'Travel'), (2, 'Banner')]),
        ),
    ]
