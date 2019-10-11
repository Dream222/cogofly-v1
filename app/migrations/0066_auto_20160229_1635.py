# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0065_auto_20160227_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnecentredinteret',
            name='centre_dinteret',
        ),
        migrations.RemoveField(
            model_name='personnecentredinteret',
            name='personne',
        ),
        migrations.RemoveField(
            model_name='personnediplome',
            name='diplome',
        ),
        migrations.RemoveField(
            model_name='personnediplome',
            name='personne',
        ),
        migrations.RemoveField(
            model_name='personnehobby',
            name='hobby',
        ),
        migrations.RemoveField(
            model_name='personnehobby',
            name='personne',
        ),
        migrations.RemoveField(
            model_name='personnelangue',
            name='langue',
        ),
        migrations.RemoveField(
            model_name='personnelangue',
            name='personne',
        ),
        migrations.RemoveField(
            model_name='personnetypepermis',
            name='personne',
        ),
        migrations.RemoveField(
            model_name='personnetypepermis',
            name='type_permis',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='centres_dinteret',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='diplomes',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='langues',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='types_permis',
        ),
        migrations.DeleteModel(
            name='PersonneCentreDInteret',
        ),
        migrations.DeleteModel(
            name='PersonneDiplome',
        ),
        migrations.DeleteModel(
            name='PersonneHobby',
        ),
        migrations.DeleteModel(
            name='PersonneLangue',
        ),
        migrations.DeleteModel(
            name='PersonneTypePermis',
        ),
    ]
