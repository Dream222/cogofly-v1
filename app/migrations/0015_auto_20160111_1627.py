# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_mur_activite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mur',
            name='relation',
            field=models.ForeignKey(default=None, blank=True, to='app.PersonneRelation', null=True, verbose_name='Relationship'),
        ),
        migrations.AlterField(
            model_name='mur',
            name='travel',
            field=models.ForeignKey(default=None, blank=True, to='app.TagWithValue', null=True, verbose_name='Travel'),
        ),
    ]
