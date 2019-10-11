# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20160209_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='personnalite',
            field=models.CharField(default='9', max_length=1, null=True, blank=True, choices=[('9', 'Other')]),
        ),
    ]
