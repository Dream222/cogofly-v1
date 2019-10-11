# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0073_personneliked_viewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='statut',
            field=models.IntegerField(default=0, choices=[(0, 'Solo')]),
        ),
    ]
