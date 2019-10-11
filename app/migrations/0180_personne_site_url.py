# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0179_auto_20160707_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='site_url',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
    ]
