# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_auto_20160210_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='profession',
            field=models.IntegerField(default=22, null=True, blank=True, choices=[(2, b'Artist'), (5, b'Chief Executive Officer'), (12, b'Civil servant'), (6, b'Clergyman'), (1, b'Craftsman'), (4, b'Driver'), (10, b'Employee'), (13, b'Engineer'), (0, b'Farmer'), (8, b'Foreman, supervisor'), (7, b'Independent retailer'), (15, b'Labourer'), (3, b'Manager'), (9, b'Managing director'), (24, b'Other'), (19, b'Pensioner'), (16, b'Policeman or Soldier'), (14, b'Primary schoolteacher'), (18, b'Self-employed profession'), (20, b'Sportsman'), (11, b'Student'), (17, b'Teacher'), (21, b'Technician'), (22, b'Undisclosed'), (23, b'Unemployed')]),
        ),
    ]
