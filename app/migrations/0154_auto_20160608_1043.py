# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0153_activiteshared_activite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='statut',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(0, 'Solo')]),
        ),
    ]
