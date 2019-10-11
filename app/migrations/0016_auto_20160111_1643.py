# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20160111_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='mur',
            name='travel_person',
            field=models.ForeignKey(default=None, blank=True, to='app.Personne', null=True, verbose_name='Personne'),
        ),
        migrations.AlterField(
            model_name='mur',
            name='activite',
            field=models.CharField(default='0', max_length=1, choices=[('1', 'has a new travel:'), ('0', 'has a new relationship:')]),
        ),
        migrations.AlterField(
            model_name='personnerelation',
            name='type_relation',
            field=models.CharField(default='0', max_length=1, choices=[('1', 'relationship'), ('0', 'friend'), ('3', 'husband <> wife'), ('2', 'parent > child'), ('4', 'teacher > student')]),
        ),
    ]
