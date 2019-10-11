# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20160111_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mur',
            old_name='travel_person',
            new_name='travel_personne',
        ),
        migrations.AlterField(
            model_name='mur',
            name='activite',
            field=models.CharField(default='0', max_length=1, choices=[('1', 'has a new travel:'), ('0', 'has a new relationship:'), ('2', 'has changed a travel:')]),
        ),
        migrations.AlterField(
            model_name='personnerelation',
            name='type_relation',
            field=models.CharField(default='0', max_length=1, choices=[('1', 'relationship'), ('0', 'friend'), ('3', 'husband / wife'), ('2', 'parent / child'), ('4', 'teacher / student')]),
        ),
    ]
