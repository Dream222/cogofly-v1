# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personne',
            name='centres_dinteret',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='diplomes',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='types_permis',
        ),
    ]
