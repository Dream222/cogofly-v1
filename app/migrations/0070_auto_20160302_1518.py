# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0069_auto_20160229_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnerelation',
            name='type_relation',
            field=models.IntegerField(default=0, choices=[(0, 'friend'), (1, 'relationship'), (2, 'parent / child'), (3, 'husband / wife'), (4, 'teacher / student'), (5, 'sent invitation / received invitation')]),
        ),
    ]
