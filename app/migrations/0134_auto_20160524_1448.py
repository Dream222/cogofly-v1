# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0133_auto_20160524_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='activites2',
            field=models.ManyToManyField(default=None, related_name='personne_activite', through='app.PersonneActivite', to='app.TagTraduit', blank=True),
        ),
        migrations.AlterField(
            model_name='personne',
            name='hobbies2',
            field=models.ManyToManyField(default=None, related_name='personne_hobby', through='app.PersonneHobby', to='app.TagTraduit', blank=True),
        ),
        migrations.AlterField(
            model_name='personne',
            name='langues2',
            field=models.ManyToManyField(default=None, related_name='personne_langue', through='app.PersonneLangue', to='app.TagTraduit', blank=True),
        ),
        migrations.AlterField(
            model_name='personne',
            name='personnalites2',
            field=models.ManyToManyField(default=None, related_name='personne_personnalite', through='app.PersonnePersonnalite', to='app.TagTraduit', blank=True),
        ),
        migrations.AlterField(
            model_name='personne',
            name='types_permis2',
            field=models.ManyToManyField(default=None, related_name='personne_typepermis', through='app.PersonneTypepermis', to='app.TagTraduit', blank=True),
        ),
    ]
