# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0124_remove_personne_personnalite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='fichier_origine',
            field=models.CharField(default=None, max_length=200, null=True, help_text="It's filled when someone adds a trip picture, you should not touch it", blank=True),
        ),
    ]
