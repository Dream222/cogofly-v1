# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0165_personne_langues2_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='est_detruit',
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
    ]
