# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0050_auto_20160224_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activite',
            name='activite',
            field=models.IntegerField(default=1, choices=[(1, 'has a new relationship:'), (2, 'has a new travel:'), (3, "has changed a travel, it's now:")]),
        ),
    ]
