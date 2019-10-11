# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app.models.generic


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0131_auto_20160524_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='programmes2',
            field=app.models.generic.ManyToManyStillValid(default=None, related_name='personne_programme', through='app.PersonneProgramme', to='app.TagTraduit', blank=True),
        ),
    ]
