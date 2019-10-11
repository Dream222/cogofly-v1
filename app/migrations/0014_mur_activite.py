# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_mur'),
    ]

    operations = [
        migrations.AddField(
            model_name='mur',
            name='activite',
            field=models.CharField(default='0', max_length=1, choices=[('1', 'has added a travel'), ('0', 'has added a relationship')]),
        ),
    ]
