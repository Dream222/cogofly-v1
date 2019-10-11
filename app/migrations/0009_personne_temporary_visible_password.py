# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20151230_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='temporary_visible_password',
            field=models.CharField(default='', max_length=200, blank=True),
        ),
    ]
