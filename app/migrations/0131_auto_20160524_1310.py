# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0130_auto_20160524_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personneactivite',
            options={'ordering': ['date_v_debut']},
        ),
        migrations.AlterModelOptions(
            name='personnehobby',
            options={'ordering': ['date_v_debut']},
        ),
        migrations.AlterModelOptions(
            name='personnelangue',
            options={'ordering': ['date_v_debut']},
        ),
        migrations.AlterModelOptions(
            name='personnepersonnalite',
            options={'ordering': ['date_v_debut']},
        ),
        migrations.AlterModelOptions(
            name='personneprogramme',
            options={'ordering': ['date_v_debut']},
        ),
        migrations.AlterModelOptions(
            name='personnetypepermis',
            options={'ordering': ['date_v_debut']},
        ),
    ]
