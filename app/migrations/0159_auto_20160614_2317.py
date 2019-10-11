# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0158_auto_20160614_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='statut',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'Solo')]),
        ),
    ]
