# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0169_auto_20160617_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='niveau_etudes',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(0, 'Nursery school'), (1, 'Primary education'), (2, 'Lower secondary education'), (3, 'Upper secondary education'), (4, 'Post-secondary non-tertiary education'), (5, 'Short-cycle tertiary education'), (6, "Bachelor's Degree or equivalent level"), (7, "Master's Degree or equivalent level"), (8, 'Ph.D. or equivalent level'), (9, 'Other'), (10, 'Not precised')]),
        ),
        migrations.AlterField(
            model_name='personne',
            name='profession',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(0, 'Farmer'), (1, 'Craftsman'), (2, 'Artist'), (3, 'Manager'), (4, 'Driver'), (5, 'Chief Executive Officer'), (6, 'Clergyman'), (7, 'Independent retailer'), (8, 'Foreman, supervisor'), (9, 'Managing director'), (10, 'Employee'), (11, 'Student'), (12, 'Civil servant'), (13, 'Engineer'), (14, 'Primary schoolteacher'), (15, 'Labourer'), (16, 'Policeman or Soldier'), (17, 'Teacher'), (18, 'Self-employed profession'), (19, 'Pensioner'), (20, 'Sportsman'), (21, 'Technician'), (22, 'Undisclosed'), (23, 'Unemployed'), (24, 'Other'), (25, 'Not precised')]),
        ),
    ]
