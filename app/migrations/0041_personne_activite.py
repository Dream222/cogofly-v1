# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_auto_20160210_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='activite',
            field=models.IntegerField(default=36, null=True, blank=True, choices=[(0, 'Administration'), (1, 'Aeronautics-Space-Defence-Navy-Armament'), (2, 'Agriculuture-Food'), (3, 'Food-Catering'), (4, 'Art-Shows-Creation'), (5, 'Associations-Social'), (6, 'Audiovisual-Cinema'), (7, 'Audit-Accounting-Management-Finance'), (8, 'Automobile'), (9, 'Banking-Insurance'), (10, 'Building-Public maintenance'), (11, 'Consumer goods-Craft'), (12, 'Commerce-Distribution'), (13, 'Advice-Services-Sales'), (14, 'Documentation-Library'), (15, 'Teaching-Research-Law'), (16, 'Maintenance-Security'), (17, 'Environment-Humanitarian work'), (18, 'Fairs-Trade fairs-Congresses'), (19, 'Civil Service'), (20, 'Hotel and Catering'), (21, 'Real Estate-Culture-Heritage'), (22, 'Printing-Editing-Books-Journalism'), (23, 'Industry-Sciences'), (24, 'IT-Web-Telecommunications-High-Tech'), (25, 'Languages-Writing-Media'), (26, 'Marketing-Communication-Advertising'), (27, 'Fashion-Textiles'), (28, 'Pharmaceuticals-Paramedical-Health-Medical'), (29, 'Politics'), (30, 'Funeral Services'), (31, 'Psychology'), (32, 'Human Resources'), (33, 'Sport'), (34, 'Tourism'), (35, 'Transport-Logistics-Rail'), (36, 'Other')]),
        ),
    ]
