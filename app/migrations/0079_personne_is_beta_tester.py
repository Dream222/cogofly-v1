# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0078_personnethrough'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='is_beta_tester',
            field=models.BooleanField(default=False),
        ),
    ]
