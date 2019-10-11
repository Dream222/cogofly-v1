# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0155_personne_niveau_visibilite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='label',
            field=models.CharField(default=None, max_length=200, blank=True, help_text='A recall of what this blog contains (language independant)', null=True, verbose_name='Label'),
        ),
    ]
