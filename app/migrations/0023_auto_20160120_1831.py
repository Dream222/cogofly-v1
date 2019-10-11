# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_personneliked_activite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='statut',
            field=models.CharField(default='0', max_length=1, choices=[('1', 'Married'), ('0', 'Single'), ('3', 'Common-law'), ('2', 'Divorced')]),
        ),
    ]
