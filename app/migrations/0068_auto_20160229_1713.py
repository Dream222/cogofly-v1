# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0067_personne_hobbies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='niveau_etudes',
            field=models.IntegerField(default=9, null=True, blank=True, choices=[(0, 'Nursery school'), (1, 'Primary education'), (2, 'Lower secondary education'), (3, 'Upper secondary education'), (4, 'Post-secondary non-tertiary education'), (5, 'Short-cycle tertiary education'), (6, "Bachelor's Degree or equivalent level"), (7, "Master's Degree or equivalent level"), (8, 'Ph.D. or equivalent level'), (9, 'Other')]),
        ),
        migrations.AlterField(
            model_name='personne',
            name='personnalite',
            field=models.IntegerField(default=14, null=True, blank=True, choices=[(0, 'Considerate'), (1, 'Adventurous'), (2, 'Calm'), (3, 'Compliant'), (4, 'Funny'), (5, 'Demanding'), (6, 'Proud'), (7, 'Generous'), (8, 'Reserved'), (9, 'Sensitive'), (10, 'Sociable'), (11, 'Spontaneous'), (12, 'Shy'), (13, 'Reliable'), (14, 'Other')]),
        ),
        migrations.AlterField(
            model_name='personne',
            name='profession',
            field=models.IntegerField(default=24, null=True, blank=True, choices=[(0, 'Farmer'), (1, 'Craftsman'), (2, 'Artist'), (3, 'Manager'), (4, 'Driver'), (5, 'Chief Executive Officer'), (6, 'Clergyman'), (7, 'Independent retailer'), (8, 'Foreman, supervisor'), (9, 'Managing director'), (10, 'Employee'), (11, 'Student'), (12, 'Civil servant'), (13, 'Engineer'), (14, 'Primary schoolteacher'), (15, 'Labourer'), (16, 'Policeman or Soldier'), (17, 'Teacher'), (18, 'Self-employed profession'), (19, 'Pensioner'), (20, 'Sportsman'), (21, 'Technician'), (22, 'Undisclosed'), (23, 'Unemployed'), (24, 'Other')]),
        ),
    ]
