# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_personne_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='langue',
            field=models.IntegerField(default=30, null=True, blank=True, choices=[(0, 'Albanian'), (1, 'German'), (2, 'British'), (3, 'Arabic'), (4, 'Armenian'), (5, '    Bengali'), (6, 'Catalan'), (7, 'Chinese'), (8, 'Korean'), (9, 'Croatian'), (10, 'Danish'), (11, 'Spanish'), (12, 'Finnish'), (13, 'French'), (14, 'Greek'), (15, 'Hungarian'), (16, 'Italian'), (17, 'Malaysian'), (18, 'Mongolian'), (19, 'Dutch'), (20, 'Occitan'), (21, 'Persian'), (22, 'Portuguese'), (23, 'Romanian'), (24, 'Russian'), (25, 'Serbian'), (26, 'Slovakian'), (27, 'Slovenian'), (28, 'Swedish'), (29, 'Turkish'), (30, 'Other')]),
        ),
        migrations.AlterField(
            model_name='personne',
            name='profession',
            field=models.IntegerField(default=22, null=True, blank=True, choices=[(0, 'Farmer'), (1, 'Craftsman'), (2, 'Artist'), (3, 'Manager'), (4, 'Driver'), (5, 'Chief Executive Officer'), (6, 'Clergyman'), (7, 'Independent retailer'), (8, 'Foreman, supervisor'), (9, 'Managing director'), (10, 'Employee'), (11, 'Student'), (12, 'Civil servant'), (13, 'Engineer'), (14, 'Primary schoolteacher'), (15, 'Labourer'), (16, 'Policeman or Soldier'), (17, 'Teacher'), (18, 'Self-employed profession'), (19, 'Pensioner'), (20, 'Sportsman'), (21, 'Technician'), (22, 'Undisclosed'), (23, 'Unemployed'), (24, 'Other')]),
        ),
    ]
