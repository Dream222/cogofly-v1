# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0192_auto_20160908_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='how_did_i_know_cogofly',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(1, 'Facebook'), (2, 'Google'), (3, 'Google_plus'), (4, 'Twitter'), (5, 'Flyers'), (6, 'Word_of_mouth'), (7, 'Other')]),
        ),
        migrations.AlterField(
            model_name='personne',
            name='newsletter_configuration',
            field=models.IntegerField(default=2, null=True, blank=True, choices=[(1, 'Every day'), (2, 'Every week'), (3, 'Every month'), (4, 'Never send news')]),
        ),
    ]
