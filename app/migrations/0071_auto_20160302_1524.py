# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0070_auto_20160302_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnerelation',
            name='type_relation',
            field=models.IntegerField(default=0, choices=[(0, 'friend'), (1, 'relationship'), (2, 'sent invitation / received invitation'), (3, 'parent / child'), (4, 'child / parent'), (5, 'husband / wife'), (6, 'wife / husband'), (7, 'teacher / student'), (8, 'student / teacher')]),
        ),
    ]
