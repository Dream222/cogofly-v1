# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0066_auto_20160229_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='hobbies',
            field=models.IntegerField(default=31, null=True, blank=True, choices=[(1, 'Charity work'), (2, 'Animals \u2013 Zoo - Nature'), (3, 'Art \u2013 Painting - Drawing'), (4, 'Cars \u2013 Motorbikes - Boats'), (5, 'Walking \u2013 Parks - Trade fairs'), (6, 'Pool - Bowling'), (7, 'DIY - Gardening'), (8, 'Antiques Fairs - Car boot sales'), (9, 'Song \u2013 Dance - Music'), (10, 'Hunting - Fishing'), (11, 'Cinema - Theatre'), (12, 'Gastronomy - Oenology'), (13, 'Decoration'), (14, 'Writing - Reading'), (15, 'Exhibitions \u2013 Museums - Castles'), (16, 'Events \u2013 Opera - Concerts'), (17, 'Fairs'), (18, 'History - Archaeology'), (19, 'IT \u2013 Web - Sciences'), (20, 'Games (cards/videos/roles)'), (21, 'Photography - Video'), (22, 'Poetry - Literature'), (23, 'Politics'), (24, 'Philosophy - Sociology'), (25, 'Restaurants - Picnics'), (26, 'Weekends away'), (27, 'Shopping'), (28, 'Sport'), (29, 'Sea \u2013 Beach \u2013 Mountains - Skiing'), (30, 'Television \u2013 Radio - Newspapers'), (31, 'Other')]),
        ),
    ]
