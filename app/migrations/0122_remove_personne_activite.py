# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0121_remove_personne_programme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personne',
            name='activite',
        ),
    ]
