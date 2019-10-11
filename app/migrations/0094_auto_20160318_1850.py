# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0093_tagbase_tagtraduit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='confirmation_code',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
    ]
