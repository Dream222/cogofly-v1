# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0193_auto_20161007_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='how_did_i_know_cogofly',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(1, 'Facebook'), (2, 'Google'), (3, 'Google Plus'), (4, 'Twitter'), (5, 'Flyers'), (6, 'Word of mouth'), (7, 'Other')]),
        ),
    ]
