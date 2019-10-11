# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20160111_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mur',
            name='travel_personne',
        ),
        migrations.AlterField(
            model_name='mur',
            name='travel',
            field=models.ForeignKey(default=None, blank=True, to='app.PersonneTravel', null=True, verbose_name='Travel'),
        ),
    ]
