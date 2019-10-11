# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0163_activitetestimony_testimony_show_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='age_visible',
            field=models.BooleanField(default=True),
        ),
    ]
