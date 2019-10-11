# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0190_auto_20160828_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='reason_delete',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]
