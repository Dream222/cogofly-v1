# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20160210_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='niveau_etudes',
            field=models.IntegerField(default=1, null=True, blank=True, choices=[(0, 'Early childhood education ("less than primary" for educational attainment)'), (1, 'Primary education'), (2, 'Lower secondary education'), (3, 'Upper secondary education'), (4, 'Post-secondary non-tertiary education'), (5, 'Short-cycle tertiary education'), (6, 'Bachelor\u2019s or equivalent level'), (7, 'Master\u2019s or equivalent level'), (8, 'Doctoral or equivalent level'), (9, 'Other')]),
        ),
        migrations.AlterField(
            model_name='personne',
            name='personnalite',
            field=models.IntegerField(default=10, null=True, blank=True, choices=[(0, 'Considerate'), (1, 'Adventurous'), (2, 'Calm'), (3, 'Compliant'), (4, 'Funny'), (5, 'Demanding'), (6, 'Proud'), (7, 'Generous'), (8, 'Reserved'), (9, 'Sensitive'), (10, 'Sociable'), (11, 'Spontaneous'), (12, 'Shy'), (13, 'Reliable'), (14, 'Other')]),
        ),
    ]
