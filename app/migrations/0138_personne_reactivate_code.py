# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0137_personne_est_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='reactivate_code',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
    ]
