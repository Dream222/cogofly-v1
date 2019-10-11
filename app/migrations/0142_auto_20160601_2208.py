# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0141_remove_personne_reactivate_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personne',
            name='est_active',
        ),
        migrations.AddField(
            model_name='personne',
            name='reactivate_code',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
    ]
