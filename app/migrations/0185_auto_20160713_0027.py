# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0184_auto_20160712_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='sexe',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(1, 'Male'), (2, 'Female')]),
        ),
    ]
