# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_personne_programme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='niveau_etudes',
            field=models.IntegerField(default=1, null=True, blank=True, choices=[(0, 'Nursery school'), (1, 'Primary education'), (2, 'Lower secondary education'), (3, 'Upper secondary education'), (4, 'Post-secondary non-tertiary education'), (5, 'Short-cycle tertiary education'), (6, "Bachelor's Degree or equivalent level"), (7, "Master's Degree or equivalent level"), (8, 'Ph.D. or equivalent level'), (9, 'Other')]),
        ),
        migrations.AlterField(
            model_name='personne',
            name='statut',
            field=models.CharField(default='0', max_length=1, choices=[('1', 'Group'), ('0', 'Solo'), ('3', 'Family'), ('2', 'Couple')]),
        ),
    ]
