# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_personneliked_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='programme',
            field=models.IntegerField(default=10, null=True, blank=True, choices=[(0, 'Education'), (1, 'Arts and humanities'), (2, 'Social sciences, journalism and information'), (3, 'Business, administration and law'), (4, 'Natural sciences, mathematics and statistics'), (5, 'Informatics and communication'), (6, 'Engineering, manufacturing and construction'), (7, 'Agriculture, forestry, fisheries and veterinary'), (8, 'Health and welfare'), (9, 'Services'), (10, 'Other')]),
        ),
    ]
