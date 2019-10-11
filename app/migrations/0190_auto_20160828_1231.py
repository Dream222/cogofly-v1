# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0189_auto_20160828_1138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personnephoto',
            options={'ordering': ['date_v_debut'], 'verbose_name': 'Person / photo', 'verbose_name_plural': 'Person / photos'},
        ),
        migrations.AlterModelOptions(
            name='personnesearch',
            options={'ordering': ['date_v_debut'], 'verbose_name': 'Person / search', 'verbose_name_plural': 'Person / searches'},
        ),
    ]
