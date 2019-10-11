# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0167_auto_20160617_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='est_fumeur',
            field=models.IntegerField(default=3, null=True, blank=True, choices=[(0, 'Non-smoker'), (1, 'Smoker'), (2, 'Social smoker'), (3, 'Not precised')]),
        ),
    ]
