# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_auto_20160224_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='custom_zodiac_sign',
            field=models.IntegerField(default=12, choices=[(0, 'Capricorn'), (1, 'Aquarius'), (2, 'Pisces'), (3, 'Aries'), (4, 'Taurus'), (5, 'Gemini'), (6, 'Cancer'), (7, 'Leo'), (8, 'Virgo'), (9, 'Libra'), (10, 'Scorpio'), (11, 'Sagittarius'), (12, 'Not precised')]),
        ),
        migrations.AlterField(
            model_name='personne',
            name='statut',
            field=models.IntegerField(default=0, choices=[(0, 'Solo'), (1, 'Group'), (2, 'Couple'), (3, 'Family')]),
        ),
    ]
