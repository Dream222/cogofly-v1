# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_personne_activite'),
    ]

    operations = [
        migrations.AddField(
            model_name='personneliked',
            name='liked',
            field=models.BooleanField(default=True),
        ),
    ]
