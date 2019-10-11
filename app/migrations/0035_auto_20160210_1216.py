# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20160210_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='personnalite',
            field=models.IntegerField(default='10', null=True, blank=True, choices=[('11', 'Spontaneous'), ('10', 'Sociable'), ('13', 'Reliable'), ('12', 'Shy'), ('14', 'Other'), ('1', 'Adventurous'), ('0', 'Considerate'), ('3', 'Compliant'), ('2', 'Calm'), ('5', 'Demanding'), ('4', 'Funny'), ('7', 'Generous'), ('6', 'Proud'), ('9', 'Sensitive'), ('8', 'Reserved')]),
        ),
    ]
