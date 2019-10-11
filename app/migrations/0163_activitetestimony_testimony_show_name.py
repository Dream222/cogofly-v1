# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0162_activitetestimony_validated_by_moderator'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitetestimony',
            name='testimony_show_name',
            field=models.BooleanField(default=False),
        ),
    ]
