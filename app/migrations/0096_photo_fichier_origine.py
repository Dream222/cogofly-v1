# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0095_auto_20160321_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='fichier_origine',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
    ]
