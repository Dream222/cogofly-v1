# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0106_auto_20160411_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnerelation',
            name='type_relation',
            field=models.IntegerField(default=0, choices=[(0, 'friend'), (1, 'relationship'), (2, 'sent invitation'), (3, 'invitation refused'), (4, 'parent / child'), (5, 'child / parent'), (6, 'husband / wife'), (7, 'wife / husband'), (8, 'teacher / student'), (9, 'student / teacher'), (10, 'remover / removed')]),
        ),
    ]
