# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20160127_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='niveau_etudes',
            field=models.CharField(default='1', max_length=1, null=True, blank=True, choices=[('1', 'Primary education'), ('0', 'Early childhood education ("less than primary" for educational attainment)'), ('3', 'Upper secondary education'), ('2', 'Lower secondary education'), ('5', 'Short-cycle tertiary education'), ('4', 'Post-secondary non-tertiary education'), ('7', 'Master\u2019s or equivalent level'), ('6', 'Bachelor\u2019s or equivalent level'), ('9', 'Other'), ('8', 'Doctoral or equivalent level')]),
        ),
        migrations.AlterField(
            model_name='personne',
            name='est_fumeur',
            field=models.CharField(default='0', max_length=1, null=True, blank=True, choices=[('1', 'Smoker'), ('0', 'Non-smoker'), ('3', 'Other'), ('2', 'Social smoker')]),
        ),
    ]
