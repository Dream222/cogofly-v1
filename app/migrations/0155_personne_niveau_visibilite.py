# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0154_auto_20160608_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='niveau_visibilite',
            field=models.IntegerField(default=1, null=True, blank=True, choices=[(1, 'Everyone can see those informations'), (2, 'Only my friends can see those informations'), (3, 'Only me can see those informations')]),
        ),
    ]
