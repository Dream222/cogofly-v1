# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0096_photo_fichier_origine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagbase',
            name='type_tag',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(1, 'Level of education'), (2, 'Job'), (3, 'Driving licences'), (4, 'Hobby'), (5, 'Driving licences'), (6, 'Personality'), (7, 'Language'), (8, 'Diploma')]),
        ),
    ]
