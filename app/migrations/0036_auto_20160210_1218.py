# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20160210_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='niveau_etudes',
            field=models.IntegerField(default='1', null=True, blank=True, choices=[('1', 'Primary education'), ('0', 'Early childhood education ("less than primary" for educational attainment)'), ('3', 'Upper secondary education'), ('2', 'Lower secondary education'), ('5', 'Short-cycle tertiary education'), ('4', 'Post-secondary non-tertiary education'), ('7', 'Master\u2019s or equivalent level'), ('6', 'Bachelor\u2019s or equivalent level'), ('9', 'Other'), ('8', 'Doctoral or equivalent level')]),
        ),
    ]
