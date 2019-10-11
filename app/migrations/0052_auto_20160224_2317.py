# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_auto_20160224_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activite',
            name='activite',
            field=models.IntegerField(default=0, choices=[(0, 'has a new relationship:'), (1, 'has a new travel:'), (2, "has changed a travel, it's now:")]),
        ),
        migrations.AlterField(
            model_name='personne',
            name='sexe',
            field=models.IntegerField(default=0, choices=[(0, 'Male'), (1, 'Female')]),
        ),
        migrations.AlterField(
            model_name='personnerelation',
            name='type_relation',
            field=models.IntegerField(default=0, choices=[(0, 'friend'), (1, 'relationship'), (2, 'parent / child'), (3, 'husband / wife'), (4, 'teacher / student')]),
        ),
    ]
