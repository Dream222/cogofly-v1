# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151229_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='centres_dinteret',
            field=models.ManyToManyField(default=None, related_name='personne_centres_dinteret', through='app.PersonneCentreDInteret', to='app.TagWithValue', blank=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='diplomes',
            field=models.ManyToManyField(default=None, related_name='personne_diplome', through='app.PersonneDiplome', to='app.TagWithValue', blank=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='hobbies',
            field=models.ManyToManyField(default=None, related_name='personne_hobby', through='app.PersonneHobby', to='app.TagWithValue', blank=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='types_permis',
            field=models.ManyToManyField(default=None, related_name='personne_type_permis', through='app.PersonneTypePermis', to='app.TagWithValue', blank=True),
        ),
    ]
