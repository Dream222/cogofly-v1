# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0079_personne_is_beta_tester'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='reset_password',
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
    ]
