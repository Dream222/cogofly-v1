# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0164_personne_age_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='langues2_visible',
            field=models.BooleanField(default=True),
        ),
    ]
