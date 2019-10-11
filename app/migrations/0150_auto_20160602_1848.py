# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0149_auto_20160602_1815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activitecomments',
            options={'ordering': ['-date_last_modif'], 'verbose_name': 'Activites / commentaire', 'verbose_name_plural': 'Activites / commentaires'},
        ),
    ]
