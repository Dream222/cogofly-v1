# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0068_auto_20160229_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='activite_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='conduite_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='custom_zodiac_sign_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='employer_current_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='employer_previous_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='est_fumeur_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='hobbies_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='langue_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='nb_enfants_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='niveau_etudes_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='personnalite_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='profession_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='programme_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='self_description_visible',
            field=models.BooleanField(default=True),
        ),
    ]
