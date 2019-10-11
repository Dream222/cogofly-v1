# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0186_auto_20160726_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagtraduit',
            name='poids',
        ),
        migrations.AddField(
            model_name='tagbase',
            name='poids',
            field=models.IntegerField(default=None, help_text='Used for ordering', null=True, blank=True),
        ),
    ]
